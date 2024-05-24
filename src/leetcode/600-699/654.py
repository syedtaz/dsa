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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def create(i: int, j: int) -> Optional[TreeNode]:
            if i > j:
                return None

            root = max(nums[i : j + 1])
            idx = nums[i : j + 1].index(root) + i

            return TreeNode(root, create(i, idx - 1), create(idx + 1, j))

        return create(0, len(nums) - 1)
