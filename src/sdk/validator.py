# src/sdk/validator.py
from pathlib import Path
from typing import Union
from .schemas.meta_schema import ModuleMetaSchema, AppMetaSchema
from .exceptions import ValidationError
from .utils.meta_parser import parse_meta_file


class ComponentValidator:
    """Validador seguro que NO ejecuta código de __meta__.py"""

    def validate_manifest(self, path: Path) -> Union[ModuleMetaSchema, AppMetaSchema]:
        """
        Valida __meta__.py en el directorio del componente

        Args:
            path: Ruta al DIRECTORIO del componente (no al archivo __meta__.py)
        """
        if not path.exists() or not path.is_dir():
            raise ValidationError(f"Ruta inválida (debe ser directorio): {path}")

        meta_path = path / "__meta__.py"
        if not meta_path.exists():
            raise ValidationError(f"Falta __meta__.py en {path}")

        # Parsear seguro con AST
        metadata_dict = parse_meta_file(meta_path)

        # Validar campos obligatorios mínimos
        required_fields = [
            "technical_name", "display_name", "component_type",
            "package_type", "python", "erp_version", "version"
        ]
        missing = [f for f in required_fields if f not in metadata_dict]
        if missing:
            raise ValidationError(f"Campos obligatorios faltantes: {', '.join(missing)}")

        # Validar según tipo de componente
        component_type = metadata_dict["component_type"]
        if component_type == "module":
            return ModuleMetaSchema(**metadata_dict)
        elif component_type == "app":
            return AppMetaSchema(**metadata_dict)
        else:
            raise ValidationError(
                f"component_type inválido: '{component_type}' "
                f"(valores permitidos: 'module', 'app')"
            )