from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed = pushed[::-1]
        popped = popped[::-1]

        stack: list[int] = []

        while len(pushed) > 0:
            if len(stack) > 0 and popped[-1] == stack[-1]:
                _ = stack.pop()
                _ = popped.pop()
                continue

            stack.append(pushed.pop())

        return stack == popped
