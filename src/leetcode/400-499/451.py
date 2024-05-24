from collections import Counter


# With sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([s * c for s, c in Counter(s).most_common()])


# Without sorting.
# Might not actually be faster lol.
class Solution2:
    def frequencySort(self, s: str) -> str:
        hashtbl = Counter(s)
        size = max(hashtbl.values())
        buckets: list[list[str]] = [[] for _ in range(size + 1)]

        for s, c in hashtbl.items():
            buckets[c].append(s)

        string: list[str] = []
        for i, c in enumerate(reversed(buckets)):
            string.extend([x * (size - i) for x in c])

        return "".join(string)
