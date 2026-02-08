class DependencyError(Exception):
    pass


class CircularDependencyError(DependencyError):
    pass


class MissingDependencyError(DependencyError):
    pass
