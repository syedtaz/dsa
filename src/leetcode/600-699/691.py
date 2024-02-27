from typing import List
from collections import Counter


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        acc: Counter[str] = Counter(target)
        counters: dict[int, Counter[str]] = {
            idx: Counter(k) for idx, k in enumerate(stickers)
        }

        def f(x: int) -> tuple[int, dict[str, int]]:
            sum_acc : int = sum(acc.values())
            a : dict[str, int] = {}

            for k, v in counters[x].items():
                if k in acc:
                    y = min(acc[k], v)
                    sum_acc = sum_acc - y
                    a[k] = y

            return sum_acc, a


        queue : list[tuple[int, dict[str, int]]] = [f(idx) for idx in range(len(stickers))]
        queue.sort(key=lambda x: x[0])
        count = 0

        while len(acc) > 0:
            size, counts = queue.pop()
            if size == 0:
                break

            count += 1
            for k, v in counts.items():
                if acc[k] <= v:
                    _ = acc.pop(k)
                else:
                    acc[k] -= v

            queue = [f(idx) for idx in range(len(stickers))]
            queue.sort(key=lambda x: x[0])

        return count if len(acc) == 0 else -1

s = Solution()
print(s.minStickers(stickers = ["notice","possible"], target = "basicbasic"))