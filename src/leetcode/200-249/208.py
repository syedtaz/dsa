class Node:
    value: str
    children: dict[str, "Node"]
    word: bool

    def __init__(self, value: str, children: dict[str, "Node"], word: bool) -> None:
        self.value = value
        self.children = children
        self.word = word


class Trie:
    root: Node

    def __init__(self) -> None:
        self.root = Node("", {}, True)

    def insert(self, word: str) -> None:
        current = self.root

        for i, char in enumerate(word):
            if char not in current.children:
                current.children[char] = Node(word[i], {}, False)
            current = current.children[char]

        current.word = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False

            current = current.children[char]

        return current.word

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True
