from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels: set[str] = {"a", "e", "i", "o", "u"}

        def at_most(k: int) -> int:
            counts: dict[str, int] = defaultdict(int)
            acc, i = 0, 0

            for j, ch in enumerate(word):
                # Skip ahead
                if ch not in vowels:
                    i = j + 1
                    counts.clear()
                    continue

                counts[ch] += 1

                # While not valid
                while len(counts) > k:
                    counts[word[i]] -= 1

                    if counts[word[i]] == 0:
                        _ = counts.pop(word[i])

                    i += 1

                acc += j - i + 1

            return acc

        return at_most(5) - at_most(4)
