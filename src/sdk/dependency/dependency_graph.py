from collections import defaultdict, deque
from .errors import CircularDependencyError


class DependencyGraph:
    """
    Grafo dirigido para dependencias de módulos/apps
    """

    def __init__(self):
        self.graph = defaultdict(set)

    def add_node(self, node: str):
        self.graph.setdefault(node, set())

    def add_dependency(self, node: str, depends_on: str):
        self.graph[node].add(depends_on)

    def topological_sort(self) -> list[str]:
        """
        Kahn's Algorithm
        """
        in_degree = {node: 0 for node in self.graph}

        for node in self.graph:
            for dep in self.graph[node]:
                in_degree[dep] = in_degree.get(dep, 0) + 1

        queue = deque([n for n, d in in_degree.items() if d == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for dep in self.graph[node]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.append(dep)

        if len(result) != len(in_degree):
            raise CircularDependencyError(
                "Dependencia circular detectada"
            )

        return result
