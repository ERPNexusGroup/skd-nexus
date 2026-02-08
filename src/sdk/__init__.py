# src/sdk/__init__.py
"""
ERP NEXUS SDK
=============
SDK puro Python para definir y validar componentes compatibles con ERP NEXUS.
"""
__version__ = "0.2.0"

# Exportar clases principales para API pública
# from bk.validator import ComponentValidator
from .schemas.meta_schema import (
    ModuleMetaSchema,
    AppMetaSchema,
    BaseMetaSchema,
)
# from bk.exceptions import (
#     NexusSDKError,
#     ValidationError,
#     DependencyError,
#     InstallationError,
# )
# from bk.contracts import StorageBackend
# from .utils.meta_parser import parse_meta_file

__version__ = "0.2.0"

# Definir API pública explícita
__all__ = [
    # Validación
    # "ComponentValidator",
    # "parse_meta_file",

    # Esquemas
    "ModuleMetaSchema",
    "AppMetaSchema",
    "BaseMetaSchema",

    # Excepciones
    # "NexusSDKError",
    # "ValidationError",
    # "DependencyError",
    # "InstallationError",

    # Contratos
    # "StorageBackend",
]