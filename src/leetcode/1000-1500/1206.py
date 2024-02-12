from typing import Optional
import random


class Node:
    value: int
    forward: list[Optional["Node"]]

    def __init__(self, value: int, level: int) -> None:
        self.value = value
        self.forward = [None] * (level + 1)


class Skiplist:
    head: Node
    level: int
    size: int

    def __init__(self) -> None:
        self.head = Node(0, 0)
        self.level = -1
        self.size = 0

    def search(self, target: int) -> bool:
        current = self.head

        for i in range(self.level):

            while True:
                if current.forward[i] is None or current.forward[i].value > target:
                    break

                assert current.forward[i] is not None
                if current.forward[i].value == target:
                    return True

                current = current.forward[i]

        return False

    def random_level(self) -> int:
        level = 0

        while random.getrandbits(32) % 2 == 0:
            level += 1

        return level

    def adjust_level(self, level: int) -> None:
        temp = self.head.forward

        self.head = Node(0, level)
        self.level = level

        for i in range(len(temp)):
          self.head.forward[i] = temp[i]

    def add(self, num: int) -> None:
        nlevel = self.random_level()

        if nlevel > self.level:
            self.adjust_level(nlevel)

        node = Node(num, nlevel)
        stack = [None] * (nlevel + 1)
        cur = self.head

        for i in range(self.level, -1, -1):
            while cur.forward[i] is not None and cur.forward[i].value < num:
                cur = cur.forward[i]
            stack[i] = cur

        for i in range(nlevel):
            node.forward[i] = stack[i].forward[i]
            stack[i].forward[i] = node

        self.size += 1

    def erase(self, num: int) -> bool:
        cur = self.head

        for i in range(self.level, -1, -1):
            while True:
                if cur.forward[i] is None or cur.forward[i].value > num:
                    break

                if cur.forward[i].value == num:
                    cur.forward[i] = cur.forward[i].forward[i]
                    return True

                cur = cur.forward[i]

        return False
