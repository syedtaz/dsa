class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        def f(a: str, b: str) -> str:
            l = len(b)
            if len(b) == 0:
                return a

            left = a.find(b)
            return f(a[:left] + a[left + l :], b) if left != -1 else a

        return f(s, part)