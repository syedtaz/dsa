class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        acc: list[str] = []

        while i < len(s):
            acc += s[i : i + k][::-1]
            i += k
            acc += s[i : i + k]
            i += k

        return "".join(acc)