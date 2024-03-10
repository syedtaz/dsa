from typing import List
from math import floor


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        m, n = len(img), len(img[0])

        def pick(i: int, j: int) -> int:
            mask = [-1, 0, 1]
            acc, count = 0, 0

            for x in mask:
                for y in mask:
                    a, b = i + x, j + y
                    if 0 <= a <= m - 1 and 0 <= b <= n - 1:
                        acc += img[a][b] % 256
                        count += 1

            return floor(acc / count)

        for i in range(m):
            for j in range(n):
                img[i][j] += pick(i, j) * 256

        for i in range(m):
            for j in range(n):
                img[i][j] //= 256

        return img
