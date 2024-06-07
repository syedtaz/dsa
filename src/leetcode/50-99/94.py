from nodedef import TreeNode
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            if node is None:
                return acc
            return fold(node.left, acc) + [node.val] + fold(node.right, acc)

        return fold(root, [])

    def inorderTraversalnonrec(self, root: Optional[TreeNode]) -> List[int]:

        acc : list[int] = []
        stack : list[TreeNode] = []
        curr : TreeNode | None = root

        while curr is not None or len(stack) > 0:

            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            acc.append(curr.val)
            curr = curr.right

        return acc

    def inorderTraversalMorris(self, root: Optional[TreeNode]) -> list[int]:

        acc : list[int] = []
        curr : TreeNode | None = root

        while curr is not None:

            if curr.left is None:
                acc.append(curr.val)
                curr = curr.right
                continue

            node = curr.left
            # Find predecessor
            while node.right is not None and node.right != curr:
                node = node.right

            if node.right == curr:
                # Destroy back edge
                node.right = None
                acc.append(curr.val)
                curr = curr.right
            else:
                # Create back edge
                node.right = curr
                curr = curr.left


        return acc