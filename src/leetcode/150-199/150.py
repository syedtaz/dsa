from typing import List, Callable

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack : list[int] = []

        def apply(f: Callable[[int, int], int]) -> None:
            a = stack.pop()
            b = stack.pop()
            stack.append(f(a, b))

        for token in tokens:
            match token:
                case '+':
                    apply(lambda a, b: a + b)
                case '-':
                    apply(lambda a, b: b - a)
                case '*':
                    apply(lambda a, b: a * b)
                case '/':
                    apply(lambda a, b: int(b / a))
                case _:
                    stack.append(int(token))

        return stack[-1]