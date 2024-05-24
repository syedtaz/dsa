class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(i: int, j: int, deleted: bool) -> bool:
            if i == j:
                return True

            if i + 1 == j:
                return s[i] == s[j] or (s[i] != s[j] and not deleted)

            if s[i] != s[j] and deleted:
                return False

            return (
                palindrome(i + 1, j - 1, False)
                if s[i] == s[j]
                else (palindrome(i + 1, j, True) or palindrome(i, j - 1, True))
            )

        return palindrome(0, len(s) - 1, False)


# s = Solution()
# print(s.validPalindrome("aba"))
# print(s.validPalindrome("abca"))
# print(s.validPalindrome("abc"))
