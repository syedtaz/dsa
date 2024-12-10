from typing import List


class ATM:
    _state: dict[int, int]
    _order: list[int] = [500, 200, 100, 50, 20]

    def __init__(self) -> None:
        self._state = {x: 0 for x in self._order}

    def deposit(self, banknotesCount: List[int]) -> None:
        for id, num in enumerate(banknotesCount[::-1]):
            self._state[self._order[id]] += num

    def withdraw(self, amount: int) -> List[int]:
        curr = amount
        choices = [0] * 5

        for id, choice in enumerate(self._order):
            if choice > curr or self._state[choice] == 0:
                continue

            spent = min(curr // choice, self._state[choice])
            choices[id] += spent
            curr -= spent * choice

        if curr == 0:
            for id, choice in enumerate(self._order):
                self._state[choice] -= choices[id]

            return choices[::-1]

        return [-1]
