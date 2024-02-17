from typing import List

class Codec:
    def map(self, s: str) -> str:
        return s.replace("/", "//")

    def inverse(self, s: str) -> str:
        return s.replace("//", "/")

    def encode(self, strs: List[str]) -> str:
        return "/:".join([self.map(x) for x in strs]) + "/:"

    def decode(self, s: str) -> List[str]:
        acc : list[str] = []
        prev = 0

        for i, j in zip(range(len(s)), range(len(s[1:]))):
            if s[i:j+2] == "/:":
                acc.append(s[prev:i])
                prev = j + 2

        return [self.inverse(x) for x in acc]