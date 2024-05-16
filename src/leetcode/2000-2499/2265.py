from nodedef import TreeNode


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        acc = 0

        def traverse(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return (0, 0)

            nonlocal acc

            l, lc = traverse(node.left)
            r, rc = traverse(node.right)

            total = l + r + node.val
            count = 1 + lc + rc

            if node.val == (total // count):
                acc += 1

            return (total, count)

        traverse(root)
        return acc