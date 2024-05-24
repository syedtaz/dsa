class Solution:
    def totalNQueens(self, n: int) -> int:
        def f(state: list[int], idx: int) -> int:
            if idx >= n:
                return 1

            acc = 0
            for j in range(n):
                legal = True
                for i in range(idx):
                    if (
                        state[i] == j
                        or state[i] == j + idx - i
                        or state[i] == j - idx + i
                    ):
                        legal = False

                if legal:
                    next = state + [j]
                    acc += f(next, idx + 1)

            return acc

        return f([], 0)
