from pathlib import Path
from .dependency_graph import DependencyGraph
from .errors import MissingDependencyError
from .version_resolver import VersionResolver
from .. import ValidationError
from ..utils.meta_parser import parse_meta_file


class DependencyResolver:

    def __init__(self):
        self.graph = DependencyGraph()
        self.components = {}

    def load_component(self, path: Path):
        path = path.resolve()

        meta_path = path / "__meta__.py"
        if not meta_path.exists():
            raise FileNotFoundError(
                f"No se encontró __meta__.py en {path}. "
                f"¿Es un componente ERP NEXUS válido?"
            )

        meta = parse_meta_file(path / "__meta__.py")

        if meta["technical_name"] != path.name:
            raise ValidationError(
                f"El directorio '{path.name}' no coincide con technical_name "
                f"'{meta['technical_name']}'"
            )

        name = meta["technical_name"]

        self.components[name] = meta
        self.graph.add_node(name)

        for dep in meta.get("depends", []):
            self.graph.add_dependency(name, dep)

    def resolve(self) -> dict:
        """
        Devuelve plan de instalación
        """
        # Validar dependencias faltantes
        for name, meta in self.components.items():
            for dep in meta.get("depends", []):
                if dep not in self.components:
                    raise MissingDependencyError(
                        f"{name} depende de {dep} que no está cargado"
                    )

        order = self.graph.topological_sort()

        return {
            "install_order": order,
            "total": len(order),
        }
