from collections import Counter


def anonymous(magazine: str, letter: str) -> bool:
    cmag = Counter(magazine)

    for k in letter:
        if k not in cmag or cmag[k] < 1:
            return False
        cmag[k] -= 1

    return True
