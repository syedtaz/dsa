from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: "Node | None"


class FrontMiddleBackQueue:
    __slots__ = ("front", "middle", "back", "sentinel")
    front: Node
    middle: Node
    back: Node
    sentinel: Node

    def __init__(self) -> None:
        self.sentinel = Node(0, None)
        self.front = self.sentinel
        self.middle = self.sentinel
        self.back = self.sentinel

    def pushFront(self, val: int) -> None:
        if self.front == self.sentinel:
            node = Node(val, None)
            self.front = self.middle = self.back = node
            self.sentinel.next = node
            return

        node = Node(val, self.front)
        self.sentinel.next = node
        return

    #   # Do some adjusting

    # def pushMiddle(self, val: int) -> None:

    def pushBack(self, val: int) -> None:
        if self.back == self.sentinel:
            self.pushFront(val)
            return

        self.back.next = Node(val, None)
        self.back = self.back.next
        # Do some adjusting for the middle
        return

    def popFront(self) -> int:
        if self.front == self.sentinel:
            return -1

        node = self.front
        if node.next is None:
            self.front = self.back = self.middle = self.sentinel
            return node.val

        self.front = node.next
        # Do some adjusting
        self.sentinel.next = self.front
        return node.val

    # def popMiddle(self) -> int:

    # def popBack(self) -> int:


s = FrontMiddleBackQueue()
s.pushFront(1)
print(s.middle)
