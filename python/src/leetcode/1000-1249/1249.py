class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i, count = 0, 0
        acc: list[str] = []

        while True:
            if i >= len(s):
                s = "".join(acc)
                acc = []
                j = len(s) - 1
                count = abs(count)

                while True:
                    if count <= 0:
                        return s[: j + 1] + "".join(acc)[::-1]

                    if s[j] == "(":
                        j, count = j - 1, count - 1
                        continue

                    acc.append(s[j])
                    j = j - 1

            elif s[i] == ")":
                if count < 0:
                    acc.append(s[i])
                    i, count = i + 1, count + 1
                else:
                    i, count = i + 1, 0

            elif s[i] == "(":
                acc.append(s[i])
                i, count = i + 1, count - 1

            else:
                acc.append(s[i])
                i = i + 1
