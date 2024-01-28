from typing import Callable, Optional

parser = Callable[[str], Optional[str]]


class Solution:
    def isNumber(self, s: str) -> bool:
        def cond(x: str, f: Callable[[str], bool]) -> Optional[str]:
            if x == "":
                return None
            return x[1:] if f(x) else None

        def sign(x: str) -> Optional[str]:
            return cond(x, lambda z: z[0] == "-" or z[0] == "+")

        def exp(x: str) -> Optional[str]:
            return cond(x, lambda z: z[0] == "e" or z[0] == "E")

        def dot(x: str) -> Optional[str]:
            return cond(x, lambda z: z[0] == ".")

        def digit(x: str) -> Optional[str]:
            return cond(x, lambda z: z[0].isdigit())

        def option(x: str, f: parser) -> Optional[str]:
            if x == "":
                return None
            res = f(x)
            return res if res is not None else x

        def repeat_once(x: str, f: parser) -> Optional[str]:
            if x == "":
                return None

            res = f(x)
            if res is None:
                return None

            next = f(res)
            while next is not None:
                res = next
                next = f(res)
            return res

        def sequence(x: str, f: parser, g: parser) -> Optional[str]:
            a = f(x)
            return g(a) if a is not None else None

        digits: parser = lambda z: repeat_once(z, digit)
        fsign: parser = lambda z: option(z, sign)
        eq: Callable[[str | None], bool] = lambda z: z is not None and z == ""
        deconly: parser = lambda z: sequence(z, digits, dot)
        decplus: parser = lambda z: sequence(z, deconly, digits)
        dotplus: parser = lambda z: sequence(z, dot, digits)

        def integer(x: str) -> Optional[str]:
            return sequence(x, fsign, digits)

        def decimal(x: str) -> Optional[str]:
            a = fsign(x)
            if a is None:
                return None

            c = decplus(a)
            if c is not None:
                return c

            b = deconly(a)
            if b is not None:
                return b

            return dotplus(a)

        def eplus(x: str) -> Optional[str]:
            if x == "":
                return ""

            f: parser = lambda z: sequence(z, exp, integer)
            return option(x, f)

        def integerf(x: str) -> Optional[str]:
            return sequence(x, integer, eplus)

        def decimalf(x: str) -> Optional[str]:
            return sequence(x, decimal, eplus)

        return eq(decimalf(s)) | eq(integerf(s))


# s = Solution()
# examples = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

# for x in examples:
#     print(s.isNumber(x))
