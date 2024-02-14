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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def fold(a: Optional[TreeNode], b : Optional[TreeNode]) -> bool:
            if a is None and b is None:
                return True

            if (a is None and b is not None) or (a is not None and b is None):
                return False

            assert a is not None and b is not None
            return a.val == b.val and fold(a.left, b.left) and fold(a.right, b.right)

        return fold(p, q)