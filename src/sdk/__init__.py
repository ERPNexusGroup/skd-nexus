# src/sdk/__init__.py
"""
ERP NEXUS SDK
=============
SDK puro Python para definir y validar componentes compatibles con ERP NEXUS.
"""
__version__ = "0.1.0"

# Exportar clases principales para API pública
from .validator import ComponentValidator
from .schemas.meta_schema import (
    ModuleMetaSchema,
    AppMetaSchema,
    BaseMetaSchema,
)
from .schemas.dependency_schema import DependencySchema
from .exceptions import (
    NexusSDKError,
    ValidationError,
    DependencyError,
    InstallationError,
)
from .contracts import StorageBackend
from .utils.meta_parser import parse_meta_file

# Definir API pública explícita
__all__ = [
    # Validación
    "ComponentValidator",
    "parse_meta_file",

    # Esquemas
    "ModuleMetaSchema",
    "AppMetaSchema",
    "LibMetaSchema",
    "BaseMetaSchema",
    "CreatorInfo",
    "DependencySchema",

    # Excepciones
    "NexusSDKError",
    "ValidationError",
    "DependencyError",
    "InstallationError",

    # Contratos
    "StorageBackend",
]