class TicTacToe:
    rows : list[int]
    cols : list[int]
    n : int
    diag : int
    adiag : int

    def __init__(self, n: int) -> None:
        self.rows, self.cols = [0] * n, [0] * n
        self.n = n
        self.diag, self.adiag = 0, 0


    def move(self, row: int, col: int, player: int) -> int:
        v = 1 if player == 1 else -1
        self.rows[row] += v
        self.cols[col] += v

        if row == col:
            self.diag += v

        if col == (self.n - row - 1):
            self.adiag += v

        for item in [self.rows[row], self.cols[col], self.diag, self.adiag]:
            if abs(item) == self.n:
                return player

        return 0
