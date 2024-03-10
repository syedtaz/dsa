from nodedef import *

from typing import Generator

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorder(start: Optional[TreeNode]) -> Generator[int, None, None]:
            cur = start
            stack: list[TreeNode] = []

            while True:
                if cur is not None:
                    stack.append(cur)
                    cur = cur.left
                    continue

                if len(stack) > 0:
                    cur = stack.pop()
                    yield cur.val
                    cur = cur.right
                    continue

                break

        seen: set[int] = set()

        for num in inorder(root):
            if num - k in seen:
                return True
            seen.add(num)

        return False


