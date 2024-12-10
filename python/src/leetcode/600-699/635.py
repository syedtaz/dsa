from typing import List, NamedTuple
from math import inf
import datetime

Timestamp = NamedTuple("Timestamp", [("ts", tuple[float, ...]), ("id", int)])

depth_d = {"Year": 0, "Month": 1, "Day": 2, "Hour": 3, "Minute": 4, "Second": 5}


def ts_to_ord(s: str, gr: tuple[str, bool] | None) -> tuple[float, ...]:
    val = [float(x) for x in s.split(":")]
    if gr is None:
        return tuple(val)

    depth, start = gr
    d = depth_d[depth]
    if start:
        for i in range(d + 1, len(val)):
            val[i] = -inf
    else:
        for i in range(d + 1, len(val)):
            val[i] = inf
    return tuple(val)


class LogSystem:
    __slots__ = "state"

    state: list[Timestamp]

    def __init__(self):
        self.state = []

    def put(self, id: int, timestamp: str) -> None:
        self.state.append(Timestamp(ts=ts_to_ord(timestamp, None), id=id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        s, e = ts_to_ord(start, (granularity, True)), ts_to_ord(
            end, (granularity, False)
        )
        ans = sorted(
            [(x, i) for (x, i) in self.state if s <= x <= e], key=lambda x: x[0]
        )
        return [i for _, i in ans]
