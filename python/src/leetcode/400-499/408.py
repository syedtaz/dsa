from itertools import groupby


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        groups: list[tuple[bool, str]] = [
            (k, "".join(list(g))) for k, g in groupby(abbr, lambda x: x.isdigit())
        ][::-1]

        i = 0
        while i < len(word):
            numeric, value = groups.pop()

            if numeric:
                i = i + int(value)
                continue

            for j, v in enumerate(value):
                if word[i + j] != v:
                    return False

            i = i + len(value)

        return i == len(word) and len(groups) == 0


# s = Solution()
# print(s.validWordAbbreviation(word = "a", abbr = "2"))
