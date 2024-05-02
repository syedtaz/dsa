from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: str
    left: Optional["Node"]
    right: Optional["Node"]


class DList:
    _head: Node | None
    _tail: Node | None
    _length: int

    def __init__(self) -> None:
        self._head, self._tail = None, None
        self._length = 0

    def add_btwn(self, data: str, before: Node | None, after: Node | None) -> Node:
        node = Node(data, before, after)
        if before == self._tail:
            self._tail = node
        if after == self._head:
            self._head = node
        self._length += 1
        return node

    def add_first(self, data: str) -> Node:
        self.add_btwn(data, None, self._head)
        assert self._head is not None
        return self._head

    def add_last(self, data: str) -> Node:
        self.add_btwn(data, self._tail, None)
        assert self._tail is not None
        return self._tail

    def remove(self, node: Node) -> Node | None:
        before, after = node.left, node.right

        if node == self._head:
            self._head = after
        else:
            before.right = after  # type: ignore

        if node == self._tail:
            self._tail = before
        else:
            after.left = before  # type: ignore

        self._length -= 1
        return before


class TextEditor:
    cursor: Node | None
    dlist: DList

    def __init__(self) -> None:
        self.cursor = None
        self.dlist = DList()

    def addText(self, text: str) -> None:
        if text == "":
            return

        iterator = iter(text)

        if self.cursor is None:
            self.cursor = self.dlist.add_first(next(iterator))

        for item in iterator:
            assert self.cursor is not None
            self.cursor = self.dlist.add_btwn(item, self.cursor, self.cursor.right)

    def deleteText(self, k: int) -> int:
        count = 0

        while self.cursor is not None and k > 0:
            self.cursor = self.dlist.remove(self.cursor)
            count += 1
            k -= 1

        return count

    def cursorLeft(self, k: int) -> str:
        while self.cursor is not None and k > 0:
            self.cursor = self.cursor.left
            k -= 1

        if self.cursor is None:
            return ""

        acc: list[str] = []
        count = 10
        cursor = self.cursor.left

        while cursor is not None and count > 0:
            acc.append(self.cursor.value)
            cursor = cursor.left
            count -= 1

        return "".join(acc[::-1])

    def cursorRight(self, k: int) -> str:
        while self.cursor is not None and k > 0:
            self.cursor = self.cursor.right
            k -= 1

        if self.cursor is None:
            return ""

        acc: list[str] = []
        count = 10
        cursor = self.cursor.left

        while cursor is not None and count > 0:
            acc.append(self.cursor.value)
            cursor = cursor.right
            count -= 1

        return "".join(acc)
