class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            opposite = char.lower() if char.isupper() else char.upper()

            if len(stack) > 0 and stack[-1] == opposite:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)