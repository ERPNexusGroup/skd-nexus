from typing import Dict, List

from .dependency_graph import DependencyGraph
from .exceptions import (
    CircularDependencyError,
    MissingDependencyError,
)


class DependencyResolver:

    def __init__(self, components_meta: Dict[str, object]):
        """
        components_meta:
        {
            "hotel_reservations": BaseMetaSchema,
            "billing_core": BaseMetaSchema
        }
        """
        self.components_meta = components_meta
        self.graph = DependencyGraph()

    def build_graph(self):

        for name, meta in self.components_meta.items():
            self.graph.add_component(name)

            for dep in meta.depends:
                if dep not in self.components_meta:
                    raise MissingDependencyError(
                        f"{name} depende de '{dep}' pero no está disponible"
                    )
                self.graph.add_dependency(name, dep)

    def resolve_install_order(self) -> List[str]:

        visited = set()
        temp = set()
        result = []

        def visit(node: str):

            if node in temp:
                raise CircularDependencyError(
                    f"Ciclo detectado en dependencias: {node}"
                )

            if node not in visited:
                temp.add(node)

                for dep in self.graph.edges(node):
                    visit(dep)

                temp.remove(node)
                visited.add(node)
                result.append(node)

        for node in self.graph.nodes():
            visit(node)

        return result
