from collections import defaultdict
import bisect


class NumberContainers:
    queues: dict[int, list[int]]
    state: dict[int, int]

    def __init__(self) -> None:
        self.queues = defaultdict(list)
        self.state = {}

    def _maybe_remove(self, index: int) -> None:
        value = self.state.get(index, None)

        if value is not None:
            i = bisect.bisect_left(self.queues[value], index)
            if self.queues[value][i] == index:
                self.queues[value].pop(i)

    def _add(self, index: int, number: int) -> None:
        self.state[index] = number
        bisect.insort_left(self.queues[number], index)

    def change(self, index: int, number: int) -> None:
        self._maybe_remove(index)
        self._add(index, number)

    def find(self, number: int) -> int:
        idxs = self.queues.get(number, [])
        return idxs[0] if len(idxs) > 0 else -1


# s = NumberContainers()
# cmds = ["find", "change", "change", "change", "change", "find", "change", "find"]
# vls = [[10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

# for cmd, v in zip(cmds, vls):
#   match cmd:
#     case "find":
#       print(s.find(v[0]))
#     case "change":
#       print(s.change(v[0], v[1]))
#     case _:
#       assert False
