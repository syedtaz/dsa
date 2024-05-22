from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        count : dict[str, int] = defaultdict(int)
        i, ans = 0, 0

        for j, ch in enumerate(s):

            count[ch] += 1

            while len(count) > k:
                lch = s[i]
                count[lch] -= 1

                if count[lch] <= 0:
                    _ = count.pop(lch)

                i += 1

            ans = max(ans, j - i + 1)

        return ans