from nodedef import TreeNode
from typing import Optional, List


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        def leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        def left_boundary(node: TreeNode, acc: list[int]) -> list[int]:
            if leaf(node):
                return acc
            elif node.left is not None:
                return left_boundary(node.left, acc + [node.val])
            elif node.right is not None:
                return left_boundary(node.right, acc + [node.val])
            return acc

        def right_boundary(node: TreeNode, acc: list[int]) -> list[int]:
            if leaf(node):
                return acc[::-1]
            elif node.right is not None:
                return right_boundary(node.right, acc + [node.val])
            elif node.left is not None:
                return right_boundary(node.left, acc + [node.val])
            return acc[::-1]

        def leaves(node: TreeNode, acc: list[int]) -> list[int]:
            if leaf(node):
                return [node.val] + acc

            left = leaves(node.left, acc) if node.left is not None else []
            right = leaves(node.right, acc) if node.right is not None else []
            return left + right

        left = left_boundary(root.left, []) if root.left is not None else []
        right = right_boundary(root.right, []) if root.right is not None else []
        lvs = leaves(root, []) if not leaf(root) else []

        return [root.val] + left + lvs + right

## ITERATIVE

class Solution2:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        def left_boundary(node: TreeNode) -> list[int]:
            acc: list[int] = []
            curr: TreeNode = node

            while True:
                if curr.left is None and curr.right is None:
                    break

                acc.append(curr.val)

                if curr.left is not None:
                    curr = curr.left
                    continue

                if curr.right is not None:
                    curr = curr.right
                    continue

            return acc

        def right_boundary(node: TreeNode) -> list[int]:
            acc: list[int] = []
            curr: TreeNode = node

            while True:
                if curr.left is None and curr.right is None:
                    break

                acc.append(curr.val)

                if curr.right is not None:
                    curr = curr.right
                    continue

                if curr.left is not None:
                    curr = curr.left
                    continue

            return acc

        def leaves(root: TreeNode) -> list[int]:
            acc: list[int] = []
            stack: list[TreeNode] = []
            curr: TreeNode | None = root

            while curr is not None or len(stack) > 0:

                while curr is not None:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                if curr.left is None and curr.right is None:
                    acc.append(curr.val)
                curr = curr.right

            return acc

        left = left_boundary(root.left) if root.left is not None else []
        right = right_boundary(root.right) if root.right is not None else []
        lvs = leaves(root) if root.left is not None or root.right is not None else []

        return [root.val] + left + lvs + right[::-1]