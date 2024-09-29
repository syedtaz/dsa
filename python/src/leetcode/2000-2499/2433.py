from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) <= 1:
            return pref

        acc: list[int] = []
        prev = 0
        for i in range(len(pref)):
            acc.append(prev ^ pref[i])
            prev = prev ^ acc[i]
        return acc
