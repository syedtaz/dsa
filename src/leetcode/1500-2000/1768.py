class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        acc: list[str] = []

        shorter = word1 if len(word1) <= len(word2) else word2
        longer = word2 if shorter == word1 else word1

        for i in range(2 * len(shorter)):
            if i % 2 == 0:
                acc.append(word1[i // 2])
            else:
                acc.append(word2[i // 2])

        for i in range(len(shorter), len(longer)):
            acc.append(longer[i])

        return "".join(acc)
