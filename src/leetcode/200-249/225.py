from collections import deque


class MyStack:
    state: deque[int]

    def __init__(self) -> None:
        self.state = deque([])

    def push(self, x: int) -> None:
        self.state.append(x)
        size = len(self.state)
        while size > 1:
            self.state.append(self.state.popleft())
            size -= 1

    def pop(self) -> int:
        return self.state.popleft()


    def top(self) -> int:
        return self.state[0]

    def empty(self) -> bool:
        return len(self.state) == 0

