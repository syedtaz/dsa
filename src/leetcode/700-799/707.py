from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional["Node"]


def iter(node: Optional["Node"], idx: int) -> Optional["Node"]:
    return node if (idx <= 0 or node is None) else iter(node.next, idx - 1)


class MyLinkedList:
    root: Node | None
    length: int

    def __init__(self) -> None:
        self.root = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        v = iter(self.root, index)
        return -1 if v is None else v.value

    def addAtHead(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val, None)
            self.length = 1
            return None

        self.root = Node(val, self.root)
        self.length += 1
        return None

    def addAtTail(self, val: int) -> None:
        if self.root is None:
            self.root = Node(val, None)
            self.length = 1
            return None

        node = iter(self.root, self.length - 1)
        assert node is not None
        node.next = Node(val, None)
        self.length += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return None

        if index == self.length:
            return self.addAtTail(val)

        if index == 0:
            self.root = Node(val, self.root)
            self.length += 1
            return

        node = iter(self.root, index - 1)
        assert node is not None
        node.next = Node(val, node.next)
        self.length += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return None

        if index == 0 and self.root is not None:
            self.root = self.root.next
            self.length -= 1
            return

        node = iter(self.root, index - 1)
        assert node is not None
        node.next = node.next.next if node.next is not None else None
        self.length -= 1
        return