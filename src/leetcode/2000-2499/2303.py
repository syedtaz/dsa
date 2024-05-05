from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        amounts: list[int] = []
        for [a, _], [b, _] in zip([[0, 0]] + brackets, brackets):
            amounts.append(b - a)

        acc = 0.0
        current = income
        for (amount, [_, rate]) in zip(amounts, brackets):
            taxable = amount if current >= amount else current
            current -= taxable
            acc += taxable * (rate / 100)

            if current == 0:
                break

        return acc