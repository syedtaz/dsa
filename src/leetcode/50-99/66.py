from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = digits[::-1]

        def add() -> list[int]:
            i, carry = 0, 1
            acc : list[int] = []

            while True:
              if i >= len(digits):
                    return acc if carry == 0 else acc + [carry]

              num = digits[i] + carry
              if num <= 9:
                  i, carry, acc = i + 1, 0, acc + [num]
              else:
                  i, carry, acc = i + 1, 1, acc + [num % 10]

        return add()[::-1]

# Tests

import hypothesis.strategies as st
from hypothesis import given


@given(number=st.integers(min_value=1))
def test_plus_one(number: int):
    s = Solution()
    digits = [int(x) for x in str(number)]
    result = s.plusOne(digits=digits)
    transformed = int("".join([str(x) for x in result]))
    assert transformed == number + 1

