from typing import Optional


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self, val: int, left: Optional["TreeNode"], right: Optional["TreeNode"]
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def depth(node: Optional["TreeNode"], acc: int) -> int:
            return (
                acc
                if node is None
                else max(depth(node.left, acc), depth(node.right, acc)) + 1
            )

        def traverse(node: Optional["TreeNode"], height: int, acc: int) -> int:
            if node is None:
                return acc

            if height == 0:
                return acc + node.val

            return traverse(node.left, height - 1, acc) + traverse(node.right, height - 1, acc)

        d = depth(root, 0)
        return traverse(root, d - 1, 0)
