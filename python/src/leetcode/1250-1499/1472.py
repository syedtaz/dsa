from dataclasses import dataclass

@dataclass
class Node:
    value: str
    prev: 'Node | None'
    next: 'Node | None'

    def __repr__(self) -> str:
        base = f"[{self.value}]"
        if self.next is not None:
            base += " -> "
            base += str(self.next)
        return base

@dataclass
class Sentinel:
    head : Node
    tail : Node

class BrowserHistory:
    homepage : str
    root : Sentinel
    curr : Node

    def __repr__(self) -> str:
        return str(self.root.head)

    def __init__(self, homepage: str) -> None:
        self.homepage = homepage
        self.curr = Node(homepage, None, None)
        self.root = Sentinel(self.curr, self.curr)

    def visit(self, url: str) -> None:
        if self.curr.next is not None:
          temp = self.curr.next
          del temp

        self.curr.next = Node(url, self.curr, None)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:

        while self.curr != self.root.head and steps > 0:
            assert self.curr.prev is not None
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.value


    def forward(self, steps: int) -> str:

        while self.curr.next is not None and steps > 0:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.value