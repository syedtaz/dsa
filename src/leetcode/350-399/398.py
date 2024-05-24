from typing import List
from collections import defaultdict
from random import choice


class Solution:
    idxs: dict[int, list[int]]

    def __init__(self, nums: List[int]) -> None:
        acc: dict[int, list[int]] = defaultdict(list)
        for idx, num in enumerate(nums):
            acc[num].append(idx)
        self.idxs = acc

    def pick(self, target: int) -> int:
        return choice(self.idxs[target])
