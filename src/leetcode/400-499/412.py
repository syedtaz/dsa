from typing import List

def f(i: int) -> str:
    match (i % 3 == 0, i % 5 == 0):
        case (True, True):
            return "FizzBuzz"
        case (True, False):
            return "Fizz"
        case (False, True):
            return "Buzz"
        case _:
            return str(i)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [f(i) for i in range(1, n + 1)]