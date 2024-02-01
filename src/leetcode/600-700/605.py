from typing import List
from functools import cache

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        @cache
        def f(i: int, k: int) -> bool:
            print(f"{i} and {k}")
            if i >= len(flowerbed) and k > 0:
                return False

            if i >= len(flowerbed) and k <= 0:
                return True

            if flowerbed[i] == 1:
                return f(i + 2, k)

            if i < len(flowerbed) - 1 and flowerbed[i] == 1 == flowerbed[i + 1]:
                return False

            no = f(i + 1, k)
            yes = False

            yes = f(i + 1, k - 1) if i < len(flowerbed) - 1 and flowerbed[i + 1] == 0 else False

            return no or yes

        return f(0, n)

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))