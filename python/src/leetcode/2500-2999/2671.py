from collections import defaultdict


class FrequencyTracker:
    state: dict[int, int]
    counts: dict[int, int]

    def __init__(self) -> None:
        self.state = defaultdict(int)
        self.counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.state[number] += 1
        current = self.state[number]
        self.counts[current] += 1

        if current > 1:
            self.counts[current - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if number not in self.state or self.state[number] == 0:
            return

        current = self.state[number]
        self.state[number] -= 1
        self.counts[current] -= 1

        if self.state[number] > 0:
            self.counts[self.state[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.counts and self.counts[frequency] > 0
