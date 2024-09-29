from typing import List
from dataclasses import dataclass
from collections import deque

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def search(i: int, acc: str) -> str:
            if i >= len(strs):
                return acc

            return (
                search(i + 1, acc)
                if len(acc) <= len(strs[i])
                else search(i + 1, strs[i])
            )

        def f(l: int, h: int, acc: str, base: str) -> str:
            if l > h:
                return acc

            mid = l + (h - l) // 2
            sub = base[: mid + 1]

            for word in strs:
                if word[0 : mid + 1] != sub:
                    return f(l, mid - 1, acc, base)

            return f(mid + 1, h, sub, base)

        shortest = search(1, strs[0])

        return f(0, len(shortest) - 1, "", shortest)