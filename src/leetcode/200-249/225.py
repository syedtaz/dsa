from collections import deque

class MyStack:
    front : deque[int]
    back : deque[int]

    def __init__(self) -> None:
        self.front = deque([])
        self.back = deque([])


    def push(self, x: int) -> None:
        self.back.append(x)
        return


    def pop(self) -> int:
        _ = self.top()
        return self.front.popleft()

    def rewind(self) -> None:
        cur = self.front
        self.front.clear()
        self.rewind_aux()

        for k in cur:
            self.front.append(k)


    def rewind_aux(self) -> None:
        if len(self.back) == 0:
            return

        x = self.back.popleft()
        self.rewind_aux()
        self.front.append(x)


    def top(self) -> int:
        self.rewind()
        return self.front[0]


    def empty(self) -> bool:
        return len(self.front) == 0 and len(self.back) == 0