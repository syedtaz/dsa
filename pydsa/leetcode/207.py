from typing import List
from collections import defaultdict
from enum import Enum

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class Status(Enum):
          NEW = 0
          ACTIVE = 1
          FINISHED = 2

        def construct(prerequisites: List[List[int]]) -> tuple[dict[int, list[int]], set[int]]:
            g : dict[int, list[int]] = defaultdict(list)
            keys : set[int] = set()

            for edges in prerequisites:
               fr = edges[1]
               to = edges[0]
               g[fr].append(to)
               keys.add(fr)
               keys.add(to)

            return g, keys

        g, keys = construct(prerequisites=prerequisites)
        status = {idx : Status.NEW for idx in keys}

        def dfs(v: int) -> bool:
          status[v] = Status.ACTIVE

          for edge in g[v]:
              if status[edge] == Status.ACTIVE:
                  return False
              elif status[edge] == Status.NEW:
                  if not dfs(edge):
                      return False

          status[v] = Status.FINISHED
          return True

        def is_acyclic(g: dict[int, list[int]]) -> bool:
          for v in keys:
            if not dfs(v):
               return False

          return True

        return is_acyclic(g)