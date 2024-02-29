from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        _, max_v = counts.most_common(1)[0]
        ntasks = sum([1 if v == max_v else 0 for v in counts.values()])

        return max(len(tasks), (max_v - 1) * (n + 1) + ntasks)