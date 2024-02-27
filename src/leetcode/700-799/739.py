from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack: list[int] = []
        results = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                x = stack.pop()
                results[x] = i - x

            stack.append(i)

        while len(stack) > 0:
            x = stack.pop()
            results[x] = 0

        return results


# s = Solution()
# print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
