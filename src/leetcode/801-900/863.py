from typing import Optional, List

class TreeNode:
    val: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def fold(node: Optional[TreeNode], acc: list[int]) -> list[int]:
            if node is None:
                return acc

            return fold(node.left, acc) + [node.val] + fold(node.right, acc)

        results = fold(root, [])
        idx = results.index(target.val)
        return results[max(idx-k,0):min(idx+k+1, len(results))]
