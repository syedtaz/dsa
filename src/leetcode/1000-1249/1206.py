from random import randint
from sys import maxsize
from math import inf
from dataclasses import dataclass


def ffs(x: int) -> int:
    return (x & -x).bit_length() - 1


def generate_level(max_level: int) -> int:
    return ffs(randint(0, maxsize) & ((1 << max_level) - 1))


@dataclass
class Node:
    value: float
    next: "Node | None"
    down: "Node | None"

    def __repr__(self) -> str:
        arrow = "" if self.next is None else " -> "
        down = "X" if self.down is None else "O"
        return f"[{self.value}, {down}]{arrow}"


class Skiplist:
    levels: list[Node]
    max_level: int
    max_so_far : int | None

    def __repr__(self) -> str:
        glob: list[str] = []

        for i in range(self.max_level):
            curr = self.levels[i]
            acc: list[str] = []

            while curr is not None:
                acc.append(str(curr))
                curr = curr.next

            glob.append("".join(acc))

        return "\n".join(glob)

    def __find_first(self) -> int | None:
        level = self.max_so_far if self.max_so_far else 0

        while level < self.max_level:
            node = self.levels[level]
            if node.next is not None and node.next.next is not None:
                return level
            level += 1

        return None

    def __init__(self) -> None:
        self.max_level = 5
        self.levels = [
            Node(-inf, Node(inf, None, None), None) for _ in range(self.max_level + 1)
        ]
        self.max_so_far = 0

    def search(self, target: int) -> bool:
        if (level := self.__find_first()) is None:
            return False

        curr = self.levels[level]

        while curr:
            while curr.next is not None and target >= curr.next.value:
                curr = curr.next

            if curr.down is None:
                return curr.value == target

            curr = curr.down

        return False

    def _add_at_level(self, head: Node, target: int) -> Node:
        curr = head

        while curr.next is not None and target > curr.next.value:
            curr = curr.next

        temp = curr.next
        curr.next = Node(target, temp, None)
        return curr.next

    def _remove_at_level(self, head: Node, target: int) -> None:
        curr = head

        while curr.next is not None and curr.next.value != target:
            curr = curr.next

        if curr.next is not None and curr.next.value == target:
            temp = curr.next.next
            curr.next = temp

    def add(self, num: int) -> None:
        prev = self._add_at_level(self.levels[self.max_level], num)
        level = generate_level(self.max_level)

        if self.max_so_far is None:
            self.max_so_far = level
        else:
            level = min(self.max_so_far, level)


        for i in range(self.max_level - 1, level - 1, -1):
            node = self._add_at_level(self.levels[i], num)
            node.down = prev
            prev = node

    def erase(self, num: int) -> bool:
        if not self.search(num):
            return False

        for head in self.levels:
            self._remove_at_level(head, num)

        return True