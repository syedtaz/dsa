from nodedef import TreeNode

from typing import Optional


def morris(root: Optional[TreeNode]) -> list[int]:

    acc : list[int] = []
    curr : TreeNode | None = root

    while curr is not None:

        if curr.left is None:
            acc.append(curr.val)
            curr = curr.right
            continue

        node = curr.left
        # Find predecessor
        while node.right is not None and node.right != curr:
            node = node.right

        if node.right == curr:
            # Destroy back edge
            node.right = None
            acc.append(curr.val)
            curr = curr.right
        else:
            # Create back edge
            node.right = curr
            curr = curr.left


    return acc


class BSTIterator:
    state: list[int]
    pointer: int

    def __init__(self, root: Optional[TreeNode]) -> None:
        self.state = morris(root)
        self.pointer = -1

    def hasNext(self) -> bool:
        return self.pointer + 1 <= len(self.state) - 1

    def next(self) -> int:
        self.pointer += 1
        return self.state[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer >= 1

    def prev(self) -> int:
        self.pointer -= 1
        return self.state[self.pointer]
