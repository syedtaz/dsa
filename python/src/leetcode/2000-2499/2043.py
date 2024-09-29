from typing import List


class Bank:
    state: list[int]
    n: int

    def _valid(self, x: int) -> bool:
        return 1 <= x <= self.n

    def __init__(self, balance: List[int]):
        self.state = [x for x in balance]
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            self._valid(account1)
            and self._valid(account2)
            and self.state[account1 - 1] >= money
        ):
            self.state[account1 - 1] -= money
            self.state[account2 - 1] += money
            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._valid(account):
            self.state[account - 1] += money
            return True

        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._valid(account) and self.state[account - 1] >= money:
            self.state[account - 1] -= money
            return True

        return False
