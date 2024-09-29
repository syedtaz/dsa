from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for op in logs:
            match op:
                case "../":
                    if count > 0:
                        count -= 1
                case "./":
                    continue
                case _:
                    count += 1

        return count