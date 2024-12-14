from nodedef import TreeNode
from typing import Optional


def traverse(root: TreeNode, target: int) -> bool:

    stack = [root]

    while stack:
        node = stack.pop()

        if node.val == target:
            return True

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    return False


class FindElements:
    root: TreeNode | None

    def __init__(self, root: Optional[TreeNode]):

        if root is None:
            self.root = None
            return

        root.val = 0
        stack = [root]

        while stack:
            node = stack.pop()
            x = node.val

            if node.left is not None:
                node.left.val = 2 * x + 1
                stack.append(node.left)

            if node.right is not None:
                node.right.val = 2 * x + 2
                stack.append(node.right)

        self.root = root

    def find(self, target: int) -> bool:
        if self.root is None:
            return False

        return traverse(self.root, target)
