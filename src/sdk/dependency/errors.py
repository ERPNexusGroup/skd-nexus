class DependencyError(Exception):
    pass


class CircularDependencyError(DependencyError):
    pass


class MissingDependencyError(DependencyError):
    pass


class VersionConflictError(DependencyError):
    pass
