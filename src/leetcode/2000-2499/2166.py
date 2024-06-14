class Bitset:
    state: int
    size: int
    card: int

    def __init__(self, size: int):
        self.state = 0
        self.size = size
        self.card = 0

    def fix(self, idx: int) -> None:
        if self.state & (1 << idx) == 0:
            self.state |= 1 << idx
            self.card += 1

    def unfix(self, idx: int) -> None:
        if self.state & (1 << idx):
            self.state ^= 1 << idx
            self.card -= 1

    def flip(self) -> None:
        self.state ^= (1 << self.size) - 1
        self.card = self.size - self.card

    def all(self) -> bool:
        return self.card == self.size

    def one(self) -> bool:
        return self.state > 0

    def count(self) -> int:
        return self.card

    def toString(self) -> str:
        rep = bin(self.state)[2:]
        return rep[::-1] + "0" * (self.size - len(rep))