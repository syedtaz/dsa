from typing import List

class SparseVector:
    values: dict[int, int]

    def __init__(self, nums: List[int]):
        self.values = {idx: v for idx, v in enumerate(nums) if v != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([v * self.values[k] for k, v in vec.values.items() if k in self.values])