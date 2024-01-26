from functools import cache


class Solution:
    def countAndSay(self, n: int) -> str:
        def group(s: str, acc: list[tuple[str, int]]) -> list[tuple[str, int]]:
            if s == "":
                return acc

            count, idx, ch = 0, 0, s[0]
            while idx <= len(s) - 1 and s[idx] == ch:
                count += 1
                idx += 1
            return group(s[idx:], acc + [(ch, count)])

        def stringify(pairs: list[tuple[str, int]]) -> str:
            return "".join([f"{c}{s}" for s, c in pairs])

        @cache
        def f(k: int) -> str:
            return "1" if k == 1 else stringify(group(f(k - 1), []))

        return f(n)


# s = Solution()
# print(s.countAndSay(4))
