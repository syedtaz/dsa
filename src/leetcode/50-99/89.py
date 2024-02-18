from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
       return [i ^ (i >> 1) for i in range(0, 1 << n)]