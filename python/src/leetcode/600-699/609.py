from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        acc : dict[str, list[str]] = defaultdict(list)

        for path in paths:
            chunks = path.split(" ")
            base = chunks[0]

            for file in chunks[1:]:
                [name, content] = file.split("(")
                content = content[:-1]
                acc[content].append(base + "/" + name)

        return [v for v in acc.values() if len(v) > 1]