from typing import Optional
from collections import deque

class Node:
    val: int
    neighbors: list["Node"]

    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        

