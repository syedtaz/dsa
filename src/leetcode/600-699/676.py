from dataclasses import dataclass


@dataclass
class Node:
    value: str
    word: bool
    children: dict[str, "Node"]


class Trie:
    root: Node

    def __init__(self) -> None:
        self.root = Node(value="", word=False, children={})

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Node(value=char, word=False, children={})
