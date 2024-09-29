from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        choices = set(
            [
                frozenset(list("qwertyuiop")),
                frozenset(list("asdfghjkl")),
                frozenset(list("zxcvbnm")),
            ]
        )

        def check(word: str) -> bool:
            s = frozenset(list(word.lower()))

            for choice in choices:
                if s.intersection(choice) == s:
                    return True

            return False

        return [word for word in words if check(word)]
