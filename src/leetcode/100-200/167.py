from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def find(i: int, j: int, t: int) -> int | None:
            if i > j:
                return None

            mid = i + (j - i) // 2
            T = numbers[mid]
            if T == t:
                return mid
            if T < t:
                return find(mid + 1, j, t)
            else:
                return find(i, mid - 1, t)

        def skip(i: int) -> int:
            if i == len(numbers) - 1:
                return i

            return i if numbers[i] != numbers[i + 1] else skip(i + 1)

        left = 0
        while left < len(numbers):
            cand = find(left + 1, len(numbers) - 1, target - numbers[left])
            if cand is not None:
                return [left + 1, cand + 1]
            else:
                left = skip(left) + 1

        return []