from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def f(i: int, acc: int) -> bool:
            if acc == 0:
                return True

            if i >= len(flowerbed):
                return False

            if flowerbed[i] == 1:
                return f(i + 2, acc)

            if i == len(flowerbed) - 1:
                return f(i + 2, acc - 1)

            return f(i + 2, acc - 1) if flowerbed[i + 1] == 0 else f(i + 1, acc)

        return f(0, n)
