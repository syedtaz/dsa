from typing import Optional
from math import log2


class Node:
    value: int
    prev: Optional["Node"]
    next: Optional["Node"]

    def __init__(self, v: int) -> None:
        self.value = v
        self.prev, self.next = None, None

    def __repr__(self) -> str:
        return f"{self.value} -> {self.next.__repr__()}"


class MRUQueue:
    n : int
    pointers: dict[int, Node]

    def __init__(self, n: int) -> None:
        head = Node(1)
        cur = head

        self.pointers = {1: head}
        self.n = n
        idxs: set[int] = {2**x for x in range(0, int(log2(n)) + 1)}
        if n not in idxs:
            idxs.add(n)

        for i in range(2, n + 1):
            node = Node(i)
            cur.next = node
            node.prev = cur
            cur = node

            if i in idxs:
                self.pointers[i] = node

    def fetch(self, k: int) -> int:
        if k == 1:
            return self.pointers[1].value

        idx = 2 ** (int(log2(k)))

        if idx == k:
            node = self.pointers[idx]
        else:
            node = self.pointers[idx]
            diff = k - idx
            while diff != 0:
                node = node.next
                diff -= 1

        # Fix prev
        assert node.prev is not None
        node.prev.next = node.next

        # Fix next
        node.prev = self.pointers[self.n]
        self.pointers[self.n].next = node

        for i in self.pointers.keys(): # always???
            self.pointers[i] = self.pointers[i].prev

        node.prev = None
        return node.value