from typing import List
from collections import defaultdict


class Node:
    __slots__ = ("parent", "locked", "children")

    parent: int
    locked: int | None
    children: list[int]

    def __init__(self, parent: int, children: list[int]) -> None:
        self.parent = parent
        self.locked = None
        self.children = children


class LockingTree:
    nodes: list[Node]

    def __init__(self, parent: List[int]):
        children: dict[int, list[int]] = defaultdict(list)

        for i, p in enumerate(parent):
            children[p].append(i)

        self.nodes = [Node(x, children[i]) for i, x in enumerate(parent)]

    def lock(self, num: int, user: int) -> bool:
        node = self.nodes[num]
        if node.locked is None:
            node.locked = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        node = self.nodes[num]
        if node.locked is None or node.locked != user:
            return False
        node.locked = None
        return True

    def _check_ancestors(self, node: Node) -> bool:
        cur = node.parent
        while cur != -1:
            p = self.nodes[cur]
            if p.locked is not None:
                return False
            cur = p.parent

        return True

    def _check_descendants(self, node: Node) -> bool:
        for child in node.children:
            if self.nodes[child].locked is not None:
                return True

        return False

    def upgrade(self, num: int, user: int) -> bool:
        node = self.nodes[num]

        if (
            node.locked is not None
            or not (self._check_ancestors(node))
            or (self._check_descendants(node))
        ):
            print(f"{node.locked=}, {self._check_ancestors(node)=}, {self._check_descendants(node)=}")
            return False

        node.locked = user
        for child in node.children:
            self.nodes[child].locked = None
        return True
