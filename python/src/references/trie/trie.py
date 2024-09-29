class Node:
    v: str
    word: bool
    children: dict[str, "Node"]

    def __init__(self, v: str) -> None:
        self.v = v
        self.children = {}
        self.word = False


class Trie:
    root: Node

    def __init__(self) -> None:
        self.root = Node("")

    def insert(self, s: str) -> None:
        current = self.root

        for i, char in enumerate(s):
            if char not in current.children:
                prefix = s[: i + 1]
                current.children[char] = Node(prefix)
            current = current.children[char]
        current.word = True

    def find(self, s: str) -> Node | None:
        current = self.root

        for char in s:
            if char not in current.children:
                return None
            current = current.children[char]

        return current if current.word else None
