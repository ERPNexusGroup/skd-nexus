from semantic_version import SimpleSpec

from ..schemas.meta_schema import BaseMetaSchema
from ..schemas.dependency_schema import DependencySchema


class DependencyValidator:

    def validate_dependencies(self, meta: BaseMetaSchema) -> None:

        # validar dependencias declaradas
        for dep in meta.depends:
            if isinstance(dep, str):
                DependencySchema(name=dep)
            elif isinstance(dep, dict):
                DependencySchema(**dep)
                if dep.get("version"):
                    try:
                        SimpleSpec(dep["version"])
                    except ValueError:
                        raise ValueError(
                            f"Especificación de versión inválida en dependencia: {dep}"
                        )
            else:
                raise ValueError(f"Dependencia inválida: {dep}")

        # validar dependencias externas python
        for lib in meta.external_dependencies.python:
            if not isinstance(lib, str):
                raise ValueError(f"Dependencia externa inválida: {lib}")
