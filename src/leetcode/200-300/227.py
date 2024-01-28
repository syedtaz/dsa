class Solution:
    def calculate(self, s: str) -> int:

        ops : set[str] = {'+', '-', '/', '*'}

        def f(i: int, prev: int | None, op: str) -> int:
            print(prev)
            if i >= len(s):
                assert prev is not None
                return prev

            if s[i] == ' ':
                return f(i + 1, prev, op)

            if s[i] in ops:
                return f(i + 1, prev, s[i])

            j = i
            next = ""
            while j <= len(s) - 1 and s[j] not in ops:
                next += s[j]
                j += 1

            next = int(next)
            if op == "":
                return f(j + 1, next, "")
            match op:
                case '+':
                    prev = 0 if prev is None else prev
                    return f(j + 1, prev + next, "")
                case '-':
                    prev = 0 if prev is None else prev
                    return f(j + 1, prev - next, "")
                case '*':
                    prev = 1 if prev is None else prev
                    return f(j + 1, prev * next, "")
                case '/':
                    prev = 1 if prev is None else prev
                    return f(j + 1, prev // next, "")
                case "":
                    return f(j + 1, prev, "")
                case _:
                    assert False

        return f(0, None, "")

s = Solution()
print(s.calculate("1+1"))