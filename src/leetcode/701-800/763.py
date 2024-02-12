from typing import List
from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        current : set[str] = set()
        acc : list[int] = []
        c = 0

        for ch in s:
            current.add(ch)
            counter[ch] -= 1
            c += 1

            if counter[ch] == 0:
                _ = counter.pop(ch)
                current.remove(ch)

                if len(current) == 0:
                    acc.append(c)
                    c = 0

        return acc