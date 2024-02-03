from typing import List, Callable
from operator import getitem

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        def f() -> Callable[[list[str]], int]:
            match ruleKey:
                case "type":
                    return lambda i: 1 if getitem(i, 0) == ruleValue else 0
                case "color":
                    return lambda i: 1 if getitem(i, 1) == ruleValue else 0
                case "name":
                    return lambda i: 1 if getitem(i, 2) == ruleValue else 0
                case _:
                    assert False
        func = f()
        return sum([func(x) for x in items])