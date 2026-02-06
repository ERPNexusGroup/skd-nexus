import json
from pathlib import Path
from typing import Union, Dict, Any
from pydantic import ValidationError as PydanticValidationError

from .schemas import ModuleSchema, AppSchema, LibSchema
from .exceptions import ValidationError
from .constants import MANIFEST_FILES

class ComponentValidator:
    """Validador de componentes Nexus."""

    def validate_manifest(self, path: Path) -> Union[ModuleSchema, AppSchema, LibSchema]:
        """Valida el manifiesto en la ruta dada."""
        if not path.exists():
            raise ValidationError(f"La ruta {path} no existe.")

        manifest_data = self._load_json(path)
        
        if path.name == MANIFEST_FILES["module"]:
            return self._validate_schema(ModuleSchema, manifest_data)
        elif path.name == MANIFEST_FILES["app"]:
            return self._validate_schema(AppSchema, manifest_data)
        elif path.name == MANIFEST_FILES["lib"]:
            return self._validate_schema(LibSchema, manifest_data)
        else:
            raise ValidationError(f"Nombre de archivo de manifiesto desconocido: {path.name}")

    def _load_json(self, path: Path) -> Dict[str, Any]:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValidationError(f"Error al decodificar JSON en {path}: {e}")
        except Exception as e:
            raise ValidationError(f"Error al leer el archivo {path}: {e}")

    def _validate_schema(self, schema_cls, data: Dict[str, Any]):
        try:
            return schema_cls(**data)
        except PydanticValidationError as e:
            raise ValidationError(f"Error de validación: {e}")
