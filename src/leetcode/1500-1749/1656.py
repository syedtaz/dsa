from typing import List

class OrderedStream:
    nodes: dict[int, str]
    pos: int
    n: int

    def __init__(self, n: int) -> None:
        self.nodes = {}
        self.pos = 1
        self.n = n

    def _flush_mut(self) -> list[str]:
        acc : list[str] = []

        while self.pos in self.nodes and self.pos <= self.n:
            acc.append(self.nodes.pop(self.pos))
            self.pos += 1

        return acc

    def insert(self, idKey: int, value: str) -> List[str]:
        self.nodes[idKey] = value
        return self._flush_mut()
