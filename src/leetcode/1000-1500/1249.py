class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack : list[str] = []

        def valid(i: int) -> str:
            res = ""

            for idx, ch in enumerate(s[i:]):
                if ch == "(":
                    stack.append(ch)
                    res += valid(idx + 1)
                elif ch == ")":
                    if len(stack) == 0:
                        return ""
                    _ = stack.pop()
                    res = "(" + res + ch
                    return res + valid(idx + 1)
                else:
                    res += ch

            return res

        return valid(0)

s = Solution()
print(s.minRemoveToMakeValid("(abcd)"))