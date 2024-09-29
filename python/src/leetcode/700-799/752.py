from typing import List
from collections import deque

state_t = tuple[int, ...]


def incr(num: int) -> int:
    num = num + 1
    return num if num != 10 else 0


def decr(num: int) -> int:
    num = num - 1
    return num if num != -1 else 9


def neighbors(node: state_t) -> list[state_t]:
    acc: list[state_t] = []

    for i in range(4):
        plus = list(node)
        minus = list(node)
        plus[i] = incr(plus[i])
        minus[i] = decr(minus[i])
        acc.append(tuple(plus))
        acc.append(tuple(minus))

    return acc


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = (0, 0, 0, 0)
        pqueue: deque[tuple[int, state_t]] = deque([(0, start)])
        seen: set[state_t] = set([start])
        invalid = set([tuple([int(x) for x in deadend]) for deadend in deadends])

        if start in invalid:
            return -1

        final = tuple([int(x) for x in target])

        while len(pqueue) > 0:
            turns, node = pqueue.popleft()

            if node == final:
                return turns

            for neighbor in neighbors(node):
                if neighbor in invalid or neighbor in seen:
                    continue

                pqueue.append((turns + 1, neighbor))
                seen.add(neighbor)

        return -1
