from typing import Optional, List


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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if root is None:
            return []

        acc : list[list[int]] = []

        def traverse(node: TreeNode, prefix: list[int]) -> None:
            if node.left is None and node.right is None:
                return acc.append(prefix + [node.val]) if sum(prefix + [node.val]) == targetSum else None

            _ = traverse(node.right, prefix + [node.val]) if node.right is not None else None
            _ = traverse(node.left, prefix + [node.val]) if node.left is not None else None

            return None

        _ = traverse(root, [])

        return acc