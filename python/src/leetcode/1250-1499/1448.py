from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(node: Optional[TreeNode], acc: int) -> None:
            nonlocal count
            if node is None:
                return None

            mvalue = max(node.val, acc)

            if acc <= node.val:
                count = count + 1

            traverse(node.left, mvalue)
            traverse(node.right, mvalue)
            return None

        traverse(root, root.val)
        return count
