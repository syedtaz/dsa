from nodedef import *
from typing import List


class Solution:
    def postorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            return (
                acc
                if node is None
                else fold(node.left, acc) + fold(node.right, acc) + [node.val]
            )

        return fold(root, [])

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        dummy = TreeNode(-1, root)
        cur = dummy
        res = []

        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                pred = cur.left

                while pred.right and pred.right != cur:
                    pred = pred.right

                if pred.right is None:
                    pred.right = cur
                    cur = cur.left
                else:
                    node = pred

                    reverse_links(cur.left, pred)

                    while node != cur.left:
                        res.append(node.val)
                        node = node.right

                    res.append(node.val)
                    reverse_links(pred, cur.left)
                    pred.right = None
                    cur = cur.right