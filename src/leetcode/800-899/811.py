from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts: defaultdict[str, int] = defaultdict(int)

        for domain in cpdomains:
            temp = domain.split(" ")
            count, parts = int(temp[0]), temp[1].split(".")
            domains = [
                ".".join(parts[len(parts) - idx - 1 :]) for idx in range(len(parts))
            ]

            for dom in domains:
                counts[dom] += count

        return [f"{count} {item}" for item, count in counts.items()]
