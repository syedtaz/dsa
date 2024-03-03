from typing import List
from dataclasses import dataclass
from math import sqrt
from collections import deque, Counter

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        @dataclass(frozen=True)
        class Point:
            id: int
            x: int
            y: int
            r: int

            def __repr__(self) -> str:
                return f"({self.x}, {self.y}, {self.r})"

        def within(a: Point, b: Point) -> bool:
            dist = sqrt(((a.x - b.x) ** 2) + ((a.y - b.y) ** 2))
            return dist <= a.r

        @dataclass
        class Edges:
            incoming: list[Point]
            outgoing: list[Point]

            def __init__(self) -> None:
                self.incoming = []
                self.outgoing = []

            def __repr__(self) -> str:
                return f"Incoming -> {self.incoming} | Outgoing -> {self.outgoing}"

        def construct(points: list[Point]) -> dict[Point, Edges]:
          g : dict[Point, Edges] = {}

          for a in points:
              for b in points:
                  if a == b:
                      continue
                  if a not in g:
                      g[a] = Edges()
                  if b not in g:
                      g[b] = Edges()

                  if within(a, b):
                      g[a].outgoing.append(b)
                      g[b].incoming.append(a)

          return g

        points = [Point(id=idx, x=p[0], y=p[1], r=p[2]) for idx, p in enumerate(bombs)]
        graph = construct(points=points)
        print(graph)

        seen : set[Point] = set()
        roots : dict[Point, Point] = {}
        stack : deque[Point] = deque([])

        def pprdfs(v: Point):
            seen.add(v)
            for edge in graph[v].incoming:
                if edge not in seen:
                    pprdfs(edge)
            stack.appendleft(v)

        def labeldfs(v: Point, r: Point):
            roots[v] = r
            for edge in graph[v].outgoing:
                if edge not in roots:
                    labeldfs(edge, r)

        for v in graph.keys():
            if v not in seen:
                pprdfs(v)

        while len(stack) > 0:
            v = stack.popleft()
            if v not in roots:
              labeldfs(v, v)

        print(roots)
        _, c = Counter(roots.values()).most_common(1)[0]
        return c


s = Solution()
# s.maximumDetonation(bombs=[[471,296,69], [90,756,164]])
print(s.maximumDetonation(bombs=[[2, 1, 3], [6, 1, 4]]))
