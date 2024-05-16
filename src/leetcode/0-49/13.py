class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        hashtbl = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        acc = hashtbl[s[0]]

        for (prev, cur) in zip(s, s[1:]):
            pvalue, cvalue = hashtbl[prev], hashtbl[cur]
            acc += cvalue

            if pvalue < cvalue:
                acc -= 2 * pvalue

        return acc