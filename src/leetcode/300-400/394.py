class Solution:
    def decodeString(self, s: str) -> str:

        def f(i: int, multiplier: int, acc: str) -> str:
            if i >= len(s):
                return acc

            print(f"{i} with {s[i]} and {multiplier} and {acc}")
            if s[i].isdigit():
                j = i + 1
                while s[j] != '[':
                    j = j + 1
                return multiplier * (acc + f(j + 1, int(s[i:j]), ""))

            if s[i] == ']':
                return multiplier * acc + f(i + 1, 1, "")

            return f(i + 1, multiplier, acc + s[i])

        return f(0, 1, "")
