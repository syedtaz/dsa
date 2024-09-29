from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        leftw, rightw = 0, 0
        i, j = 0, 0

        while True:
            if leftw >= len(word1) and rightw >= len(word2):
                return True

            if (
                leftw >= len(word1)
                and rightw < len(word2)
                or (rightw >= len(word2) and leftw < len(word1))
            ):
                return False

            if word1[leftw][i] != word2[rightw][j]:
                return False

            i, j = i + 1, j + 1
            if i >= len(word1[leftw]):
                i, leftw = 0, leftw + 1

            if j >= len(word2[rightw]):
                j, rightw = 0, rightw + 1
