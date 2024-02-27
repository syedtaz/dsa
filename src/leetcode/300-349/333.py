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
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def fold(node: TreeNode, acc: list[int]) -> list[int]:
            match node.left is None, node.right is None:
                case True, True:
                    return [1]
                case False, False:
                    assert node.left is not None and node.right is not None
                    if node.left.val <= node.val <= node.right.val:
                        left = fold(node.left, acc)
                        right = fold(node.right, acc)
                        here = [sum(left) + sum(right) + 1]
                        return left + right + here
                    else:
                        return [0]
                case False, True:
                    assert node.left is not None
                    return fold(node.left, acc)
                case True, False:
                    assert node.right is not None
                    return fold(node.right, acc)
                case _:
                    assert False

        res = fold(root, [])
        return max(res[:-1]) if len(res) > 1 else max(res)
