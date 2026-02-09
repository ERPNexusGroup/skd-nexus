from semantic_version import Version, SimpleSpec
from .errors import VersionConflictError


class VersionResolver:

    @staticmethod
    def is_compatible(version: str, spec: str) -> bool:
        try:
            v = Version(version)
            s = SimpleSpec(spec)
            return s.match(v)
        except ValueError:
            return False

    @staticmethod
    def validate(version: str, spec: str, name: str):
        if not VersionResolver.is_compatible(version, spec):
            raise VersionConflictError(
                f"{name} versión {version} no cumple {spec}"
            )
