from typing import List
from functools import cache


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def map(i: str) -> list[str]:
            match i:
                case "2":
                    return ["a", "b", "c"]
                case "3":
                    return ["d", "e", "f"]
                case '4':
                    return ["g", "h", "i"]
                case "5":
                    return ["j", "k", "l"]
                case "6":
                    return ["m", "n", "o"]
                case "7":
                    return ["p", "q", "r", "s"]
                case "8":
                    return ["t", "u", "v"]
                case "9":
                    return ["w", "x", "y", "z"]
                case _:
                    raise KeyError

        @cache
        def f(s: str) -> list[str]:
            if s == "":
                return []

            hd = map(s[0])
            tl = f(s[1:])

            return [i + j for i in hd for j in tl] if len(tl) > 0 else hd

        return f(digits)

# s = Solution()
# print(s.letterCombinations(""))