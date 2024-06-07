from typing import Optional


class TreeNode:
    val: int
    left: "Optional[TreeNode]"
    right: "Optional[TreeNode]"

    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    T = Optional[TreeNode]
