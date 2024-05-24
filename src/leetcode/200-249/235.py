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
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> TreeNode:
        def f(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            return (
                f(node.left, p, q)
                if p.val < node.val and q.val < node.val
                else (
                    f(node.right, p, q)
                    if p.val > node.val and q.val > node.val
                    else node
                )
            )

        return f(root, p, q)
