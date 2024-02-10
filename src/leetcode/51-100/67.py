class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def pad(x: str, y: str) -> tuple[str, str]:
            if len(x) == len(y):
                return x, y
            bigger = x if len(x) > len(y) else y
            smaller = y if bigger == x else x
            diff = len(bigger) - len(smaller)
            return bigger, "0" * diff + smaller

        x, y = pad(a, b)

        def f(i: int, carry: bool) -> tuple[str, bool]:
            match x[i], y[i], carry:
                case ("1", "1", True):
                    return "1", True
                case ("1", "0", False) | ("0", "1", False) | ("0", "0", True):
                    return "1", False
                case ("1", "1", False) | ("1", "0", True) | ("0", "1", True):
                    return "0", True
                case ("0", "0", False):
                    return "0", False
                case _, _, _:
                    raise Exception

        def add(i: int, carry: bool, acc: str) -> str:
            if i == 0:
                v, c = f(i, carry)
                return "1" + v + acc if c else v + acc

            v, c = f(i, carry)
            return add(i - 1, c, v + acc)

        return add(len(x) - 1, False, "")