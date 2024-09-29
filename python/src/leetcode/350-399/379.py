class PhoneDirectory:
    state: set[int]

    def __init__(self, maxNumbers: int) -> None:
        self.state = set(range(maxNumbers))

    def get(self) -> int:
        if len(self.state) == 0:
            return -1

        return self.state.pop()


    def check(self, number: int) -> bool:
        return number in self.state

    def release(self, number: int) -> None:
        self.state.add(number)