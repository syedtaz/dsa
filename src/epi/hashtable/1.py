from collections import Counter


def palindrome_permute(word: str) -> bool:
    return sum([1 if v % 2 == 1 else 0 for v in Counter(word).values()]) <= 1
