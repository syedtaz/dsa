from typing import List


class Cashier:
    prices: dict[int, int]
    discount: float
    count: int
    n: int

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.prices = {k: v for k, v in zip(products, prices)}
        self.count, self.n, self.discount = 0, n, ((100 - discount) / 100)

    def getBill(self, product: List[int], amount: List[int]) -> float:
        discount = False
        self.count += 1

        if self.count == self.n:
            self.count = 0
            discount = True

        value = sum([self.prices[id] * am for id, am in zip(product, amount)])
        return value * self.discount if discount else value
