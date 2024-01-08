from typing import List, Callable
from dataclasses import dataclass
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        @dataclass(frozen=True)
        class T:
            time: int
            amount: int
            location: str

            def __repr__(self) -> str:
                return f"{self.time},{self.amount},{self.location}"

        def f(v: str) -> T:
            vs = v.split(",")
            time = int(vs[1])
            amount = int(vs[2])
            location = vs[3]
            return T(time=time, amount=amount, location=location)

        def s(n: str, item: T) -> str:
            return f"{n},{str(item)}"

        temp: dict[str, list[T]] = defaultdict(list)
        name: Callable[[str], str] = lambda x: x.split(",")[0]

        for t in transactions:
            temp[name(t)].append(f(t))

        mapping = {
            name: sorted(value, key=lambda x: x.time) for name, value in temp.items()
        }

        amount: set[str] = set()
        for n, lst in mapping.items():
            for item in filter(lambda x: x.amount > 1000, lst):
                amount.add(s(n, item))

        time: set[str] = set()
        for n, lst in mapping.items():
            for a, b in filter(
                lambda t: abs(t[0].time - t[1].time) <= 60
                and t[0].location != t[1].location,
                zip(lst, lst[1:]),
            ):
                A = s(n, a)
                B = s(n, b)
                if A not in amount or B not in amount:
                  time.add(f"{n},{str(b)}")
                  time.add(f"{n},{str(a)}")

        return list(time.union(amount))


# s = Solution()
# print(s.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
