from nodedef import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def f(node: TreeNode | None) -> TreeNode:
            if node is None:
                assert False

            if p.val > node.val and q.val > node.val:
                return f(node.right)

            if p.val < node.val and q.val < node.val:
                return f(node.left)

            return node

        return f(root)