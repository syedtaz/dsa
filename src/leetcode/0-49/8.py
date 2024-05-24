class Solution:
    def myAtoi(self, s: str) -> int:
        digits: set[str] = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        S = s.strip()

        if len(S) == 0:
            return 0

        def split(idx: int) -> str:
            acc = ""
            while True:
                if idx >= len(S) or S[idx] not in digits:
                    return acc
                idx, acc = idx + 1, S[idx] + acc

        def sign_start(x: str) -> tuple[bool, int]:
            assert len(x) > 0
            match x[0]:
                case "+":
                    return False, 1
                case "-":
                    return True, 1
                case _:
                    return False, 0

        def value(xs: str) -> int:
            count, acc = 0, 0

            for x in xs:
                acc += int(x) * (10**count)
                count += 1

            return acc

        def clamp(x: int) -> int:
            b = 2**31
            if x <= b * -1:
                return b * -1
            elif x >= b - 1:
                return b - 1
            return x

        isneg, start = sign_start(S)
        return clamp(value(split(start)) * (-1 if isneg else 1))


# s = Solution()
# print(s.myAtoi("asdsa123a00"))
