class Solution:
    def maxDepth(self, s: str) -> int:
        acc = 0
        stack = 0

        for char in s:
            if char == "(":
                stack += 1
                acc = max(stack, acc)
            elif char == ")":
                stack -= 1

        return acc
