from typing import List
from itertools import groupby


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:

        meetings.sort(key=lambda lst: lst[2])
        keepers: set[int] = {0, firstPerson}

        for _, lst in groupby(meetings, key=lambda x: x[2]):
            elements: set[int] = set()

            for [a, b, _] in list(lst):
                elements.add(a)
                elements.add(b)

            if any([x in keepers for x in elements]):
                keepers = keepers.union(elements)

        return list(keepers)