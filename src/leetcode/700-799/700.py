from nodedef import *

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None

            if node.val == val:
                return node

            return search(node.right) if node.val < val else search(node.left)

        return search(root)