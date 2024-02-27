from collections import defaultdict

class FreqStack:
    counts: dict[int, int]
    levels: dict[int, list[int]]
    max_level : int


    def __init__(self):
        self.counts = defaultdict(int)
        self.levels = defaultdict(list)
        self.max_level = 1

    def push(self, val: int) -> None:
        self.counts[val] += 1
        level = self.counts[val]
        self.levels[level].append(val)
        self.max_level = max(level, self.max_level)
        return

    def pop(self) -> int:
        x = self.levels[self.max_level].pop()
        self.counts[x] -= 1
        if len(self.levels[self.max_level]) == 0 and self.max_level != 1:
            self.levels.pop(self.max_level)
            self.max_level = max(self.levels.keys())
        return x