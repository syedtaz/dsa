from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort(key=lambda x: x[0])

        def intercept(a: tuple[int, int], b: tuple[int, int], x: int) -> int:




        return []

s = Solution()
print(s.outerTrees(trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))