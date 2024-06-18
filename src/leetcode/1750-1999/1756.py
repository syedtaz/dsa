
class MRUQueue:
    state : list[int]

    def __init__(self, n: int) -> None:
        self.state = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        item = self.state.pop(k - 1)
        self.state.append(item)
        return item