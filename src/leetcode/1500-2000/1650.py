# Definition for a Node.
class Node:
    val: int

    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        start = q.parent
        parents : set['Node'] = set([q])
        while start is not None:
            if start == p:
                return p

            parents.add(start)
            start = start.parent

        start = p.parent

        while start is not None:
            if start in parents:
                return start
            start = start.parent

        return q


