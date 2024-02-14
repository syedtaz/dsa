from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        if len(chars) <= 2:
            return len(chars)

        i, j, count = 0, 1, 1

        while True:
            if j >= len(chars) and count > 1:
                i = i + 1
                chars[i] = str(count)
                break

            if j >= len(chars):
                break

            if chars[i] != chars[j]:
                chars[i + 1] = str(count)
                i, j, count = i + 2, j + 1, 1
                continue

            j, count = j + 1, count + 1
            if count > 9:
                chars[i + 1] =

        return i + 1
