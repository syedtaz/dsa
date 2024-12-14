class Node:
    value: str
    count: int
    children: dict[str, 'Node']

    def __init__(self, value: str) -> None:
        self.value = value
        self.count = 0
        self.children = {}

class Trie:
    root: Node

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]

        cur.count += 1
        return

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        return cur.count

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root

        for c in prefix:
          if c not in cur.children:
            return 0
          cur = cur.children[c]

        root = cur
        acc = 0

        stack = [root]
        while stack:
            node = stack.pop()
            acc += node.count

            for childnode in node.children.values():
                stack.append(childnode)

        return acc

    def erase(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return
            cur = cur.children[c]

        cur.count -= 1