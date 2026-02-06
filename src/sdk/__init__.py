"""
ERP NEXUS SDK
=============
SDK puro Python para definir y validar módulos, aplicaciones y librerías compatibles con ERP NEXUS.
"""
__version__ = "0.1.0"

# Exportación de clases principales (API pública del SDK)
from .validator import ComponentValidator
from .installer import TransactionalInstaller
from .exceptions import (
    NexusSDKError,
    ValidationError,
    DependencyError,
    InstallationError,
)
from .contracts import StorageBackend
from .schemas import ModuleSchema, AppSchema, LibSchema

# Definir __all__ para controlar la API pública
__all__ = [
    "ComponentValidator",          # Alias amigable para ComponentValidator
    "TransactionalInstaller",
    "StorageBackend",
    "ModuleSchema",
    "AppSchema",
    "LibSchema",
    "NexusSDKError",
    "ValidationError",
    "DependencyError",
    "InstallationError",
]