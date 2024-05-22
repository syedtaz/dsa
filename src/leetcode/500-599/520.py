class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) <= 1:
            return True

        if word[0].islower():
            return word[1:].islower()

        return word[1:].islower() or word[1:].isupper()