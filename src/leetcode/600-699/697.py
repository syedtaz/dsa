from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

      def generate(nums: list[int]) -> dict[int, tuple[int, int, int]]:
        state: dict[int, tuple[int, int, int]] = {}

        for idx, num in enumerate(nums):
          if num not in state:
              state[num] = (1, idx, idx)
              continue

          count, minidx, _ = state[num]
          state[num] = (count + 1, minidx, idx)

        return state

      def find(state: dict[int, tuple[int, int, int]]) -> int:
         key = max([count for (count, _, _) in state.values()])
         positions = [end - start + 1 for count, start, end in state.values() if count == key]
         return min(positions)

      return find(generate(nums))