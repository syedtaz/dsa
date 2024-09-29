from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:

        worker.sort()
        jobs = [(pr, diff) for pr, diff in zip(profit, difficulty)]
        jobs.sort(key=lambda x: x[0])
        acc : int = 0

        while len(worker) > 0 and len(jobs) > 0:
            pr, diff = jobs[-1]

            if worker[-1] >= diff:
                worker.pop()
                acc += pr
            else:
                jobs.pop()

        return acc