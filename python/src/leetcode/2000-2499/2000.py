class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return (
            word
            if not (idx := word.find(ch))
            else word[: idx + 1][::-1] + word[idx + 1 :]
        )
