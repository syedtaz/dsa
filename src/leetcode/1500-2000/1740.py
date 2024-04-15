from nodedef import *


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:

        paths: list[int] = []
        depths: list[int] = []

        def euler(node: TreeNode, depth: int) -> None:
            paths.append(node.val)
            depths.append(depth)

            if node.left:
                euler(node.left, depth + 1)
                paths.append(node.val)
                paths.append(depth)

            if node.right:
                euler(node.right, depth + 1)
                paths.append(node.val)
                depths.append(depth)

        euler(root, 0)
        i, j = sorted((paths.index(p), paths.index(q)))
        k = min(range(i, j + 1), key=lambda x: depths[x])
        return depths[i] + depths[j] - (2 * depths[k])
