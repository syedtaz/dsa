class Node:
    value: str
    word: bool
    children: dict[str, "Node"]

    def __init__(self, value: str, word: bool, children: dict[str, "Node"]) -> None:
        self.value = value
        self.word = word
        self.children = children


class WordDictionary:
    root: Node

    def __init__(self):
        self.root = Node("", False, {})

    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node(ch, False, {})
            current = current.children[ch]

        current.word = True
        return None

    def search_aux(self, i: int, word: str, node: Node) -> bool:
        current = node

        for ch in word[i:]:
            if ch == ".":
                for child in current.children:
                    if self.search_aux(i + 1, word, current.children[child]):
                        return True
                return False
            else:
                if ch not in current.children:
                    return False
                current = current.children[ch]

        return current.word

    def search(self, word: str) -> bool:
        return self.search_aux(0, word, self.root)
