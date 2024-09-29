from nodedef import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def fold(node: TreeNode | None, acc: int) -> int:
            return acc if node is None else node.val + fold(node.right, acc)

        def fmap(node: TreeNode | None) -> TreeNode | None:
            if node is None:
                return None

            return TreeNode(
                val=fold(node, 0), left=fmap(node.left), right=fmap(node.right)
            )

        return fmap(root)
