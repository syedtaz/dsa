# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    val : int
    left : 'Optional[TreeNode]'
    right : 'Optional[TreeNode]'

    def __init__(self, val: int =0, left: 'Optional[TreeNode]' =None, right: 'Optional[TreeNode]' =None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

      if root is None:
          return True

      node = root
      cur = node
      prev = None

      while cur is not None:
          if cur.left is None:
              if prev is None:
                  prev = cur.val
              else:
                  if prev > cur.val:
                      return False
                  else:
                      prev = cur.val
              cur = cur.right
          else:
              x = cur.left
              while x.right is not None and x.right != cur:
                  x = x.right
              if x.right == cur:
                  x.right = None
                  if prev is None:
                    prev = cur.val
                  else:
                    if prev > cur.val:
                      return False
                    else:
                      prev = cur.val
                  cur = cur.right
              else:
                  x.right = cur
                  cur = cur.left

      return True

