from nodedef import *

from collections import deque


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        def search(start: TreeNode, tgt: TreeNode) -> str:
            queue: deque[tuple[str, TreeNode]] = deque([("", start)])

            while len(queue) > 0:
                path, node = queue.popleft()

                if node == tgt:
                    return path

                if node.left is not None:
                    queue.append((path + "L", node.left))

                if node.right is not None:
                    queue.append((path + "R", node.right))

            assert False

        path = search(original, target)
        current = cloned

        for ch in path:
            match ch:
                case "L":
                    current = current.left
                case "R":
                    current = current.right
                case _:
                    assert False

        return current
