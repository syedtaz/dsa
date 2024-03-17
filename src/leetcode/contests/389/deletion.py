from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        base = Counter(word)
        new : dict[str, int] = {}

        for k1, v1 in base.items():
            for k2, v2 in base.items():
                if k1 == k2:
                    continue

                if abs(v1 - v2) > k:
                    new[k1] = v1
                    break

        minimum = len(word)

        for k1, v1 in new.items():
            count : list[int] = []
            for k2, v2 in new.items():
                if k1 == k2:
                    continue

                count.append(abs(v1 - v2))

            minimum = min(minimum, sum(count) - k)

        print(new)
        return minimum



s = Solution()
print(s.minimumDeletions(word = "aabcaba", k = 0))
print(s.minimumDeletions(word = "dabdcbdcdcd", k = 2))
print(s.minimumDeletions(word = "aaabaaa", k = 2))