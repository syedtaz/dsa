class Solution:
    def isValid(self, s: str) -> bool:
        map: dict[str, str] = {"(": ")", "{": "}", "[": "]"}
        stack: list[str] = []

        for ch in s:
            if ch in map:
                stack.append(map[ch])
                continue

            if len(stack) == 0 or stack[-1] != ch:
                return False

            _ = stack.pop()

        return len(stack) == 0