# Definition for a Node.
class Node:
    val: int
    children: list["Node"]

    def __init__(
        self, val: int | None = None, children: list["Node"] | None = None
    ) -> None:
        self.val = val  # type: ignore
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: "Node") -> int:

        def depth(node: Node) -> tuple[int, int]:
            if len(node.children) == 0:
                return 0, 0

            if len(node.children) == 1:
                return 1, 0

            results = sorted([depth(x) for x in node.children], key = lambda z: z[0])
            da, db = results[0][0], results[1][0]
            results.sort(key = lambda z: z[1])
            pa = results[0][1]

            return 1 + da, max(pa, da + db + 1)

        a, b = depth(root)
        return max(a, b)
