class Solution:
    def calculate(self, s: str) -> int:

        operands: list[int] = []
        operators: list[str] = []

        def unwind_mult() -> None:
            while len(operators) > 0 and (operators[-1] == "*" or operators[-1] == "/"):
                a = operands.pop()
                b = operands.pop()
                op = operators.pop()

                if op == "*":
                    operands.append(a * b)
                else:
                    operands.append(int(b / a))

        def traverse(i: int) -> None:
            if i >= len(s):
                return

            match s[i]:
                case " ":
                    traverse(i + 1)
                case "+" | "-" | "*" | "/":
                    operators.append(s[i])
                    traverse(i + 1)
                case _:

                    acc = ""

                    while i < len(s) and s[i] not in {"+", "-", "*", "/", " "}:
                        acc += s[i]
                        i += 1

                    operands.append(int(acc))
                    unwind_mult()

                    return traverse(i)

        traverse(0)

        while len(operators) > 0:
            a = operands.pop()
            b = operands.pop()
            op = operators.pop()

            if op == "+":
                operands.append(a + b)
            else:
                operands.append(b - a)

        return operands.pop()
