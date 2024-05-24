from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for first, second in zip(matrix, matrix[1:]):
            if first[:-1] != second[1:]:
                return False

        return True


# s = Solution()
# print(s.isToeplitzMatrix(matrix = [[1,2],[2,2]]))
