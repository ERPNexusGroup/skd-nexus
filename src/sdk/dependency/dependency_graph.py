from collections import defaultdict
from typing import Dict, List, Set


class DependencyGraph:

    def __init__(self):
        self.graph: Dict[str, Set[str]] = defaultdict(set)

    def add_component(self, name: str):
        if name not in self.graph:
            self.graph[name] = set()

    def add_dependency(self, component: str, dependency: str):
        self.graph[component].add(dependency)

    def nodes(self):
        return self.graph.keys()

    def edges(self, node: str):
        return self.graph[node]
