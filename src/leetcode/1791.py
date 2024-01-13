from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][1] if edges[0][1]==edges[1][0] or edges[0][1]==edges[1][1] else edges[0][0]