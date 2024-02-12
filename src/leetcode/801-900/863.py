from typing import Optional, List
import math


class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, x: int) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def distance(node: Optional["TreeNode"], acc: int) -> int | float:
            return (
                math.inf
                if node is None
                else (
                    acc
                    if node == target
                    else min(
                        distance(node.left, acc + 1), distance(node.right, acc + 1)
                    )
                )
            )



        print(distance(root, 0))
        return []
