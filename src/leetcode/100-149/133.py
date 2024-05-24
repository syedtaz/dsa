from typing import Optional


class Node:
    val: int
    neighbors: list["Node"]

    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        seen: dict[Node, Node] = {}

        def clone(n: Node) -> Node:
            if n in seen:
                return seen[n]

            new = Node(n.val, [])
            seen[n] = new
            new.neighbors = [clone(x) for x in n.neighbors]
            return new

        return clone(node)
