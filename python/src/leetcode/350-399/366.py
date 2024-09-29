from nodedef import TreeNode
from typing import Optional, List
from collections import defaultdict

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        level_set : dict[int, list[int]] = defaultdict(list)

        def height(node: TreeNode | None) -> int:

            if node is None:
                return -1

            left = height(node.left)
            right = height(node.right)
            h = max(left, right) + 1

            level_set[h].append(node.val)
            return h

        height(root)
        levels = [(k, v) for k, v in level_set.items()]
        levels.sort(key=lambda x: x[0])
        return [v for _, v in levels]