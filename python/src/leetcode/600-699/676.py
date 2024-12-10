from typing import List


class Node:
    char: str
    end: bool
    children: dict[str, "Node"]

    def __init__(self, char: str) -> None:
        self.char = char
        self.end = False
        self.children = {}


def insert(node: Node, word: str) -> None:
    cur = node
    for c in word:
        if c not in cur.children:
            cur.children[c] = Node("c")
        cur = cur.children[c]

    cur.end = True
    return None


class MagicDictionary:
    root: Node

    def __init__(self):
        self.root = Node("")

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            insert(self.root, word)

    def search(self, searchWord: str) -> bool:
        stack: list[tuple[Node, int, int]] = [(self.root, 0, 0)]

        while stack:
            node, count, left = stack.pop()

            if count >= 2:
                continue

            if node.end and left == len(searchWord) and count == 1:
                return True

            if left == len(searchWord):
                continue

            for child, child_node in node.children.items():
                if child == searchWord[left]:
                    stack.append((child_node, count, left + 1))
                else:
                    stack.append((child_node, count + 1, left + 1))

        return False