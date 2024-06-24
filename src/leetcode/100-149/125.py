class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = "".join([x.lower() for x in s if x.isalnum()])
        return S == S[::-1]