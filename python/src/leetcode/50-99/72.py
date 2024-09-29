from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) > 0:
            return len(word2)
        elif len(word2) == 0 and len(word1) > 0:
            return len(word1)
        elif len(word1) == len(word2) == 0:
            return 0

        @cache
        def recurrence(i: int, j: int) -> int:
            if i == 0:
                return j
            elif j == 0:
                return i
            else:
                insert = 1 + recurrence(i - 1, j)
                delete = 1 + recurrence(i, j - 1)
                if word1[i] == word2[j]:
                    swap = recurrence(i - 1, j - 1)
                else:
                    swap = 1 + recurrence(i - 1, j - 1)
                return min(insert, delete, swap)

        return recurrence(len(word1) - 1, len(word2) - 1)
