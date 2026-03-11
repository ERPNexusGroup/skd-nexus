from pathlib import Path

from ..utils.meta_parser import parse_meta_file
from ..utils.validation_utils import ValidationUtils
from ..exceptions import ValidationError


class StructureValidator:

    REQUIRED_FILES = ["__meta__.py"]

    def validate_structure(self, component_path: Path) -> None:

        if not component_path.exists():
            raise FileNotFoundError(f"Componente no encontrado: {component_path}")

        if not component_path.is_dir():
            raise ValueError(f"Componente inválido (no es directorio): {component_path}")

        for file in self.REQUIRED_FILES:
            if not (component_path / file).exists():
                raise ValueError(f"Falta archivo obligatorio: {file}")

        meta_path = component_path / "__meta__.py"
        if not ValidationUtils.validate_python_syntax(meta_path):
            raise ValidationError(f"__meta__.py tiene errores de sintaxis: {meta_path}")

        # Validar que el nombre del directorio coincide con technical_name
        meta = parse_meta_file(meta_path)
        technical_name = meta.get("technical_name")
        if technical_name and technical_name != component_path.name:
            raise ValidationError(
                f"El directorio '{component_path.name}' no coincide con technical_name '{technical_name}'"
            )

        # Regla mínima para módulos con modelos: si declara models, debe existir core/models.py
        registry_flags = meta.get("registry_flags") or {}
        if isinstance(registry_flags, dict) and registry_flags.get("models") is True:
            core_models = component_path / "core" / "models.py"
            if not core_models.exists():
                raise ValidationError("registry_flags.models=True requiere core/models.py")
