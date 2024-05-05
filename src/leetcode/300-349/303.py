from typing import List


class NumArray:
    _prefixes: list[int]

    def __init__(self, nums: List[int]) -> None:
        acc = 0
        self._prefixes = [0] + [acc := acc + x for x in nums]

    def sumRange(self, left: int, right: int) -> int:
        return self._prefixes[right + 1] - self._prefixes[left]