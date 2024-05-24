from typing import Callable


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        map: Callable[[str], str] = lambda x: "01" if x == "0" else "10"

        def f(i: int, acc: str) -> str:
            if i == n:
                return acc[k - 1]

            return f(i + 1, "".join([map(x) for x in acc]))

        return int(f(0, "0"))
