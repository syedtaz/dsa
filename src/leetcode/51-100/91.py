from string import ascii_uppercase


class Solution:
    def numDecodings(self, s: str) -> int:

        mapping = {str(v): k for v, k in enumerate(ascii_uppercase)}

        def match(x: str) -> list[str]:
            return [mapping[key] for key in mapping if x[: len(key)] == key]

        A : set[str] = set()

        def f(x: str) -> str | None:
            if x == "":
                return x

            for s in s
