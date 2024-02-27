class Solution:
    def reverseWords(self, s: str) -> str:
        acc: list[str] = []
        temp: list[str] = []
        prev: bool = True

        for i in range(len(s)):
            if s[i] == " " and prev:
                continue

            if s[i] == " " and not prev:
                acc.append("".join(temp))
                prev = True
                temp = []
                continue

            temp.append(s[i])
            prev = False

        if len(temp) > 0:
            acc.append("".join(temp))

        return " ".join(acc[::-1])