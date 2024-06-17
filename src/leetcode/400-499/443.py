from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0

        while i < len(chars):

            ch = chars[i]
            count = 1
            j = i + 1

            while j < len(chars) and chars[j] == ch:
                count += 1
                j += 1

            if count == 1:
                chars[k] = ch
            else:
                chars[k] = ch

                for s in str(count):
                    k += 1
                    chars[k] = s

            k += 1
            i = j

        return k