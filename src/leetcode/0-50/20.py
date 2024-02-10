class Solution:
    def isValid(self, s: str) -> bool:
        map : dict[str, str] = {')': '(', '}': '{', ']': '['}
        opening: set[str] = {'(', '[', '{'}
        stack : list[str] = []

        for ch in s:
            if ch in opening:
                stack.append(ch)
                continue

            if len(stack) == 0 or stack[-1] != map[ch]:
                return False

            _ = stack.pop()

        return len(stack) == 0




