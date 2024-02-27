class MyQueue:
    front: list[int]
    back: list[int]


    def __init__(self) -> None:
        self.front = []
        self.back = []


    def push(self, x: int) -> None:
        self.back.append(x)
        return


    def pop(self) -> int:
        _ = self.peek()
        return self.front.pop()


    def peek(self) -> int:
        if len(self.front) == 0:
            self.front = self.back[::-1]
            self.back = []

        return self.front[-1]


    def empty(self) -> bool:
        return len(self.front) == 0 and len(self.back) == 0