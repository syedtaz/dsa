from nodedef import TreeNode
from typing import Optional, Callable


pair_t = tuple[int, int]
pair_ts = list[pair_t]
fold_t = Callable[[int, pair_ts, pair_ts, int], pair_ts]


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def fold(node: TreeNode | None, f: fold_t, acc: pair_ts, level: int) -> pair_ts:
            if node is None:
                return acc

            return f(
                node.val,
                fold(node.left, f, acc, level + 1),
                fold(node.right, f, acc, level + 1),
                level,
            )

        left_then_right = fold(
            root, lambda n, left, right, lvl: left + [(n, lvl)] + right, [], 0
        )
        right_then_left = fold(
            root, lambda n, left, right, lvl: right + [(n, lvl)] + left, [], 0
        )
        return left_then_right == right_then_left

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        def f(a: TreeNode | None, b: TreeNode | None) -> bool:
            match (a, b):
                case (None, None):
                    return True
                case (None, _) | (_, None):
                    return False
                case (a, b):
                    return a.val == b.val and f(a.left, b.right) and f(a.right, b.left)

        return not root or f(root.left, root.right)
