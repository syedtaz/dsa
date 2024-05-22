class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def count(char: str, limit: int) -> int:
            acc, i, curr = 0, 0, 0

            for j, ch in enumerate(answerKey):
                curr += 1 if ch == char else 0

                while curr > limit:
                    left = answerKey[i]
                    curr -= 1 if left == char else 0
                    i += 1

                acc = max(acc, j - i + 1)

            return acc

        return max(count("T", k), count("F", k))
