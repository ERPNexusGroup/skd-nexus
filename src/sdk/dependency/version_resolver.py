from typing import Dict, Tuple

from semantic_version import Version, SimpleSpec

from .exceptions import DependencyError


class VersionConflictError(DependencyError):
    pass


class VersionResolver:

    def __init__(self, components_meta: Dict[str, object]):
        """
        components_meta:
        {
            "billing_core": BaseMetaSchema,
            "hotel_reservations": BaseMetaSchema
        }
        """
        self.components_meta = components_meta

    def _parse_dependency(self, dep: str) -> Tuple[str, str | None]:
        """
        Convierte:
        billing_core>=1.0.0 -> ("billing_core", ">=1.0.0")
        billing_core -> ("billing_core", None)
        """
        operators = [">=", "<=", "==", "!=", ">", "<"]

        for op in operators:
            if op in dep:
                name, spec = dep.split(op, 1)
                return name.strip(), op + spec.strip()

        return dep.strip(), None

    def validate_versions(self):

        for component_name, meta in self.components_meta.items():

            for dep in meta.depends:

                dep_name, spec = self._parse_dependency(dep)

                if dep_name not in self.components_meta:
                    raise DependencyError(
                        f"{component_name} depende de {dep_name} que no existe"
                    )

                if spec is None:
                    continue

                dep_meta = self.components_meta[dep_name]

                if not self._is_compatible(dep_meta.version, spec):
                    raise VersionConflictError(
                        f"{component_name} requiere {dep_name}{spec} "
                        f"pero está instalada versión {dep_meta.version}"
                    )

    def _is_compatible(self, version: str, spec: str) -> bool:

        try:
            v = Version(version)
            s = SimpleSpec(spec)
            return s.match(v)
        except ValueError:
            raise DependencyError(
                f"Spec inválido '{spec}'"
            )
