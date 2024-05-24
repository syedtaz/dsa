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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def fold(node: Optional[TreeNode], acc: str) -> str:
            return (
                "#" + acc
                if node is None
                else "^" + str(node.val) + fold(node.left, acc) + fold(node.right, acc)
            )

        return fold(subRoot, "#") in fold(root, "#")
