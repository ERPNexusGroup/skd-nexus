class NexusSDKError(Exception):
    """Clase base para excepciones del SDK Nexus."""
    pass

class ValidationError(NexusSDKError):
    """Error durante la validación de un componente."""
    pass

class DependencyError(NexusSDKError):
    """Error relacionado con la resolución de dependencias."""
    pass

class InstallationError(NexusSDKError):
    """Error durante la instalación de un componente."""
    pass
