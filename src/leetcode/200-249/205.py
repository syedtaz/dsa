# class Solution:
# def isIsomorphic(self, s: str, t: str) -> bool:

#     if len(s) != len(t):
#         return False

#     def label(input: str) -> list[int]:
#         map : dict[str, int] = {}

#         for idx, ch in enumerate(input):
#             if ch in map:
#                 continue
#             map[ch] = idx

#         return [map[x] for x in input]

#     return label(s) == label(t)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping: dict[str, str] = {}

        for a, b in zip(s, t):
            if (a in mapping and mapping[a] != b) or (b in mapping):
                return False

            mapping[a] = b

        return True
