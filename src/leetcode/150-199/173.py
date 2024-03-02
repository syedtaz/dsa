from nodedef import *
from typing import Generator


class BSTIterator:
    iterator: Generator[int, None, None]
    next_item: int | None

    def __init__(self, root: Optional[TreeNode]) -> None:
        self.iterator = self._inorder(root)
        self._advance_iterator()

    def _advance_iterator(self) -> None:
        try:
            self.next_item = next(self.iterator)
        except StopIteration:
            self.next_item = None

    def _inorder(self, start: Optional[TreeNode]) -> Generator[int, None, None]:
        cur = start
        stack: list[TreeNode] = []

        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
                continue

            if len(stack) > 0:
                cur = stack.pop()
                yield cur.val
                cur = cur.right
                continue

            break

    def next(self) -> int:
        x = self.next_item
        assert x is not None
        self._advance_iterator()
        return x

    def hasNext(self) -> bool:
        return self.next_item is not None
