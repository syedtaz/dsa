from typing import Callable


class Solution:
    def isNumber(self, s: str) -> bool:

        def digit(x: str) -> str:
            if x == "":
                return ""
            return x[1:] if x[0].isdigit() else x

        print(digit("123"))
        return False

s = Solution()
s.isNumber("")