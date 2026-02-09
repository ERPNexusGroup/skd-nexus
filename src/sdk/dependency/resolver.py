from pathlib import Path
from .dependency_graph import DependencyGraph
from .errors import MissingDependencyError
from .version_resolver import VersionResolver
from .. import ValidationError, BaseMetaSchema
from ..utils.meta_parser import parse_meta_file


class DependencyResolver:

    def __init__(self):
        self.graph = DependencyGraph()
        self.components: dict[str, BaseMetaSchema] = {}

    def load_component(self, path: Path):
        path = path.resolve()
        meta_path = path / "__meta__.py"

        if not meta_path.exists():
            raise FileNotFoundError(f"No se encontró __meta__.py en {path}")

        meta_dict = parse_meta_file(meta_path)
        meta = BaseMetaSchema(**meta_dict)

        if meta.technical_name != path.name:
            raise ValidationError(
                f"El directorio '{path.name}' no coincide con technical_name '{meta.technical_name}'"
            )

        self.components[meta.technical_name] = meta
        self.graph.add_node(meta.technical_name)

        for dep in meta.depends:
            self.graph.add_dependency(meta.technical_name, dep)

    def resolve(self) -> dict:
        """
        Devuelve plan de instalación
        """
        # Validar dependencias faltantes
        for name, meta in self.components.items():
            for dep in meta.depends:
                if dep not in self.components:
                    raise MissingDependencyError(
                        f"'{name}' depende de '{dep}', "
                        f"pero no está cargado. Disponibles: {list(self.components.keys())}"
                    )

        order = self.graph.topological_sort()

        return {
            "install_order": order,
            "total": len(order),
        }
