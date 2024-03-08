from collections import defaultdict
from typing import List

index = tuple[str, int]

def nodify(s: str) -> index:
    letters = [x for x in s if x.isalpha()]
    nums = [x for x in s if x.isnumeric()]
    return "".join(letters), int("".join(nums))

class DependencyGraph:
    graph: dict[index, set[index]]

    def __init__(self) -> None:
        self.graph = defaultdict(set)

    def deps(self, x: index) -> set[index]:
        return self.graph[x]

    def add(self, source: index, value: index) -> None:
        self.graph[source].add(value)
        return None

    def clear(self, x: index) -> None:
        for _, v in self.graph.items():
            v.discard(x)
        return None

class Excel:
    table: dict[index, int]
    depgraph: DependencyGraph
    summations: dict[index, list[index]]

    def __init__(self, height: int, width: str):
        self.table = {}
        self.depgraph = DependencyGraph()

    def set(self, row: int, column: str, val: int) -> None:
        self.table[(column, row)] = val

        for dep in self.depgraph.deps((column, row)):
            self._update(dep)

    def get(self, row: int, column: str) -> int:
        return self.table[(column, row)]

    def _update(self, node: index) -> int:
        acc = 0
        for dep in self.summations[node]:
            acc += self.table[dep]
        self.table[node] = acc
        return acc

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        node = (column, row)
        self.depgraph.clear(node)

        if len(numbers) == 1:
            target = nodify(numbers[0])
            self.summations[node] = [target]
            self.depgraph.add(source=target, value=node)
            return self._update(node)



