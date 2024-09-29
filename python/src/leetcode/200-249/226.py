from typing import Optional
from nodedef import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None

            node.left, node.right = f(node.right), f(node.left)
            return node

        return f(root)

    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack : list[TreeNode | None] = [root]

        while len(stack) > 0:
            node = stack.pop()

            if node is None:
                continue

            node.left, node.right = node.right, node.left
            stack.append(node.right)
            stack.append(node.left)


        return root
