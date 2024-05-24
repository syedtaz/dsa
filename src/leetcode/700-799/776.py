from typing import Optional, List


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
    def splitBST(
        self, root: Optional[TreeNode], target: int
    ) -> List[Optional[TreeNode]]:
        def f(
            node: Optional[TreeNode], parent: TreeNode, target: int
        ) -> List[Optional[TreeNode]]:
            if node is None:
                return [root, None]

            if node.val <= target:
                match (node.left, node.right):
                    case _, None:
                        parent.left = None
                        return [node, root]
                    case _, rchild:
                        if rchild.val > target:
                            parent.left = rchild
                            node.right = None
                            return [node, root]
                        else:
                            parent.left = None
                            return [node, root]

            return f(node.left, node, target)

        if root is None or root.val <= target:
            return [root, None]

        return f(root.left, root, target)
