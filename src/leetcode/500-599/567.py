class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def count(s: str) -> list[int]:
            acc = [0] * 26
            for x in s:
                acc[ord(x) - 97] += 1
            return acc

        target = count(s1)
        current = count(s2[: len(s1)])

        for i in range(len(s2) - len(s1)):
            if current == target:
                return True

            current[ord(s2[i]) - 97] -= 1
            current[ord(s2[i + len(s1)]) - 97] += 1

        return current == target
