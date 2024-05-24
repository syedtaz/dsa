class Solution:
    def checkString(self, s: str) -> bool:
        b = False

        for char in s:
            if char == "a" and b:
                return False

            if char == "b":
                b = True

        return True
