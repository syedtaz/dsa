import random

class Node:
    left: 'Node | None'
    right: 'Node | None'
    value: str
    score: int

    def __init__(self, value: str, score: int, left : "Node | None" = None, right: 'Node | None' = None) -> None:
        self.value, self.score, self.left, self.right = value, score, left, right

class SORTracker:
    root: Node

    def __init__(self) -> None:
      self.root = Node("", random.randint(0, 50_000))

    def add(self, name: str, score: int) -> None:
        node = self.root

        while node is not None:
            if node.score < score:
                node = node.right
            else:



    def get(self) -> str:
