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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if root is None:
            return 0

        def compare(
            left: tuple[int, float], right: tuple[int, float]
        ) -> tuple[int, float]:
            match (left[1] <= right[1], left[0] < right[0]):
                case (True, True):
                    return left
                case _:
                    return right

        def fold(node: Optional[TreeNode], acc: tuple[int, float]) -> tuple[int, float]:
            if node is None:
                return acc

            cur = (node.val, abs(target - node.val))
            acc = compare(cur, acc)
            left = fold(node.left, acc)
            right = fold(node.right, acc)
            return compare(left, right)

        v, _ = fold(root, (root.val, abs(target - root.val)))
        return v
