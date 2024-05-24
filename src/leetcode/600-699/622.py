from typing import Optional
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: Optional["Node"]


class MyCircularQueue:
    head: Optional["Node"]
    tail: Optional["Node"]
    n: int
    cur: int

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.n = k
        self.cur = 0

    def enQueue(self, value: int) -> bool:
        if self.cur == self.n:
            return False

        if self.head is None:
            node = Node(val=value, next=None)
            self.head = node
            self.tail = node
            self.cur += 1
            return True

        tail = self.tail
        node = Node(val=value, next=None)
        tail.next = node
        self.tail = node
        self.cur += 1
        return True

    def deQueue(self) -> bool:
        if self.cur == 0:
            return False

        head = self.head
        self.head = head.next
        self.cur -= 1

        if self.cur == 0:
            self.tail = None

        return True

    def Front(self) -> int:
        if self.cur == 0:
            return -1

        return self.head.val

    def Rear(self) -> int:
        if self.cur == 0:
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        return self.cur == 0

    def isFull(self) -> bool:
        return self.cur == self.n
