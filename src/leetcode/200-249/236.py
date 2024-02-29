from typing import Optional


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
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        def split(left: list[TreeNode], right: list[TreeNode]) -> TreeNode:
            candidate = left[0]

            for a, b in zip(left[1:], right[1:]):
                if a != b:
                    return candidate
                candidate = a

            return candidate

        ppath : list[TreeNode] = []
        qpath : list[TreeNode] = []

        def path(node: TreeNode, acc: list[TreeNode]) -> None:
            nonlocal ppath, qpath

            if len(ppath) > 0 and len(qpath) > 0:
                return

            if node == p:
                ppath = acc + [node]

            if node == q:
                qpath = acc + [node]

            if node.left is not None:
                path(node.left, acc + [node])

            if node.right is not None:
                path(node.right, acc + [node])

            return

        return split(ppath, qpath)
