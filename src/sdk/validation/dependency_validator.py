from ..schemas.meta_schema import BaseMetaSchema


class DependencyValidator:

    def validate_dependencies(self, meta: BaseMetaSchema) -> None:

        # validar nombres técnicos básicos
        for dep in meta.depends:
            if not isinstance(dep, str) or not dep:
                raise ValueError(f"Dependencia inválida: {dep}")

        # validar dependencias externas python
        for lib in meta.external_dependencies.python:
            if not isinstance(lib, str):
                raise ValueError(f"Dependencia externa inválida: {lib}")
