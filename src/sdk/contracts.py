from __future__ import annotations

from pathlib import Path
from typing import Optional, Protocol


class StorageBackend(Protocol):
    """
    Contrato de almacenamiento para instalación/desinstalación.
    Implementado por CLI y/o Core ERP.
    """

    def copy_files(self, source: Path, destination: Path) -> None:
        """Copia archivos desde el origen al destino."""
        ...

    def remove_files(self, path: Path) -> None:
        """Elimina archivos o directorios en la ruta especificada."""
        ...

    def register_component(self, path: Path, manifest: dict) -> None:
        """Registra un componente en el sistema."""
        ...

    def unregister_component(self, name: str) -> None:
        """Desregistra un componente del sistema."""
        ...

    def resolve_dependency(self, name: str, version_spec: str) -> Optional[Path]:
        """Resuelve la ruta de una dependencia instalada."""
        ...

    def get_default_install_path(self, component_name: str) -> Path:
        """Devuelve la ruta por defecto de instalación."""
        ...
