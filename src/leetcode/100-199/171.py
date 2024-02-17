from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        map = {c: idx + 1 for idx, c in enumerate(ascii_uppercase)}

        i, acc = len(columnTitle) - 1, 0

        while i > 0:
            x = columnTitle[i]

            acc += map[x] * (26 ** (len(columnTitle) - i))
            i -= 1

        return acc


s = Solution()
print(s.titleToNumber("AB"))
