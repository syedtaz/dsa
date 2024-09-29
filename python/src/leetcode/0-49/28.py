class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return False

        target = hash(needle)
        i, j = 0, len(needle) - 1

        while j != len(haystack):
            if hash(haystack[i : j + 1]) == target:
                return i
            i, j = i + 1, j + 1

        return -1

class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        target = hash(needle)

        for i in range(len(haystack) - len(needle) + 1):
            if hash(haystack[i:i + len(needle)]) == target:
                return i

        return -1