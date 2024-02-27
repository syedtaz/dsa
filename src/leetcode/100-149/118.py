from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        f = [[1], [1, 1]]

        for i in range(2, numRows):
            f[i] = [1] + [a + b for (a, b) in zip(f[i - 1], f[i - 1][1:])] + [1]

        return f
