from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from .contracts import StorageBackend
from .exceptions import InstallationError
from .schemas.meta_schema import BaseMetaSchema
from .validation.component_validator import ComponentValidator
from .dependency.install_plan import build_install_plan, InstallPlan
from .utils.meta_parser import parse_meta_file


HookRunner = Callable[[str, Path, BaseMetaSchema], None]


@dataclass(frozen=True)
class InstallResult:
    name: str
    version: str
    installed_path: Path


class TransactionalInstaller:
    """
    Instalador transaccional minimalista.
    - Valida metadata antes de instalar.
    - Copia archivos al destino.
    - Registra componente en el backend.
    - Rollback automático ante fallos.
    """

    def __init__(self, storage: StorageBackend, hook_runner: Optional[HookRunner] = None):
        self.storage = storage
        self.hook_runner = hook_runner
        self.validator = ComponentValidator()

    def install(self, source_path: Path, target_path: Optional[Path] = None) -> InstallResult:
        source_path = source_path.resolve()
        if not source_path.exists():
            raise InstallationError(f"Fuente no encontrada: {source_path}")

        # Validación de manifest y estructura
        meta = self.validator.validate_component(source_path)
        manifest = parse_meta_file(source_path / "__meta__.py")

        install_path = target_path or self.storage.get_default_install_path(meta.technical_name)
        install_path = install_path.resolve()

        registered = False
        try:
            # Hook pre_install (opcional)
            if self.hook_runner and meta.lifecycle.pre_install:
                self.hook_runner(meta.lifecycle.pre_install, source_path, meta)

            # Copiar archivos
            self.storage.copy_files(source_path, install_path)

            # Registrar componente
            self.storage.register_component(install_path, manifest)
            registered = True

            # Hook post_install (opcional)
            if self.hook_runner and meta.lifecycle.post_install:
                self.hook_runner(meta.lifecycle.post_install, install_path, meta)

            return InstallResult(
                name=meta.technical_name,
                version=meta.version,
                installed_path=install_path,
            )
        except Exception as e:
            # Rollback defensivo
            try:
                if registered:
                    self.storage.unregister_component(meta.technical_name)
                self.storage.remove_files(install_path)
            except Exception as rollback_error:
                raise InstallationError(
                    f"Error al instalar '{meta.technical_name}': {e}. "
                    f"Además falló el rollback: {rollback_error}"
                ) from rollback_error

            raise InstallationError(f"Error al instalar '{meta.technical_name}': {e}") from e

    def install_plan(self, component_paths: list[Path]) -> InstallPlan:
        """
        Construye y devuelve un plan de instalación con orden de dependencias.
        """
        return build_install_plan(component_paths)

    def install_many(self, component_paths: list[Path]) -> list[InstallResult]:
        """
        Instala múltiples componentes respetando el orden de dependencias.
        """
        plan = build_install_plan(component_paths)
        results: list[InstallResult] = []

        for name in plan.install_order:
            source_path = plan.paths_by_name.get(name)
            if source_path is None:
                raise InstallationError(
                    f"Plan inválido: no se encontró ruta para '{name}'"
                )
            results.append(self.install(source_path))

        return results

    def uninstall(self, component_name: str, installed_path: Optional[Path] = None) -> None:
        """
        Desinstala un componente por nombre. Si no se pasa ruta, usa la ruta default.
        """
        target_path = installed_path or self.storage.get_default_install_path(component_name)
        try:
            self.storage.remove_files(target_path)
            self.storage.unregister_component(component_name)
        except Exception as e:
            raise InstallationError(f"Error al desinstalar '{component_name}': {e}") from e
