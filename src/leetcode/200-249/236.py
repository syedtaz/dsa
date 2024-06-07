from nodedef import TreeNode
from typing import NamedTuple

LCA = NamedTuple("LCA", [("count", int), ("ancestor", TreeNode | None)])


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def f(node: TreeNode | None, a: TreeNode, b: TreeNode) -> LCA:
            if node is None:
                return LCA(count=0, ancestor=None)

            left = f(node.left, a, b)
            right = f(node.right, a, b)

            match (left.count, right.count):
                case (2, _):
                    return left
                case (_, 2):
                    return right
                case (_, _):
                    here = (a, b).count(node) + left.count + right.count
                    return LCA(count=here, ancestor=node if here == 2 else None)

        return f(root, p, q).ancestor  # type: ignore
