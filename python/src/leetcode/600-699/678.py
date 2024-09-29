class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0

        for c in s:
            left += 1 if c == "(" else -1
            right += 1 if c != ")" else -1
            if right < 0:
                break
            left = max(left, 0)

        return left == 0
