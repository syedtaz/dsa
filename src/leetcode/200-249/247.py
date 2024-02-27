from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        cases = {'0', '1', '8'}

        def f(i: int) -> list[str]:
            if i == 1:
                return ['0', '1', '8']

            if i == 2:
                return ['11', '69', '96', '88']

