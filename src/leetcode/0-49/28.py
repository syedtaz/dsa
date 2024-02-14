class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return False

        target = hash(needle)
        i, j = 0, len(needle) - 1

        while j != len(haystack):
            if hash(haystack[i:j+1]) == target:
                return i
            i, j = i + 1, j + 1

        return -1