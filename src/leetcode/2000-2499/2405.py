class Solution:
    def partitionString(self, s: str) -> int:

        seen: set[str] = set()
        acc: list[str] = []
        curr: list[str] = []

        for k in s:
            if k in seen:
                acc.append("".join(curr))
                curr = []
                seen.clear()

            curr.append(k)
            seen.add(k)

        if len(curr) > 0:
            acc.append("".join(curr))

        return len(acc)
