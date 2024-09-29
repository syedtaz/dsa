from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        cost = 0
        n = len(costs) // 2
        for i in range(0, n):
            cost += costs[i][0]
        for j in range(n, len(costs)):
            cost += costs[j][1]
        return cost
