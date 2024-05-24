from typing import List


class Node:
    value: str
    children: dict[str, "Node"]
    word: bool

    def __init__(self, value: str) -> None:
        self.value = value
        self.children = {}
        self.word = False


class Trie:
    root: Node

    def __init__(self) -> None:
        self.root = Node("")
        self.root.word = True

    def insert(self, word: str) -> bool:
        current = self.root

        for _, char in enumerate(word):
            if not current.word:
                return False

            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

        current.word = True
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort()

        acc = ""
        for word in words:
            res = trie.insert(word)
            if res and len(word) > len(acc):
                acc = word

        return acc
