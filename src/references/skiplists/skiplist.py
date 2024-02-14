from typing import Optional


class Node:
    value: int
    next: Optional["Node"]
    up: Optional["Node"]
    down: Optional["Node"]

    def __init__(
        self, value: int, next: Optional["Node"] = None, down: Optional["Node"] = None
    ) -> None:
        self.value = value
        self.next = next
        self.down = down

    def __repr__(self) -> str:
        return f"{self.value} -> {self.next.__repr__()}\n{self.down.__repr__()}"


def level_search(node: Node, v: int) -> Node | None:
    if node.value == v:
        return node
    if node.next is None:
        return None
    return node if node.next.value > v else level_search(node.next, v)


def search(node: Node, v: int) -> Node | None:
    cand = level_search(node, v)
    if cand is None:
        return None

    if cand.value == v:
        return cand

    return search(cand.down, v) if cand.down is not None else None
