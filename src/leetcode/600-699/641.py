class MyCircularDeque:
    front: list[int]
    back: list[int]
    k: int
    cur: int

    def __init__(self, k: int) -> None:
        self.front = []
        self.back = []
        self.k = k
        self.cur = 0

    def insertFront(self, value: int) -> bool:
        if self.cur == self.k:
            return False

        self.front.append(value)
        self.cur += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.cur == self.k:
            return False

        if len(self.front) == 0:
            self.front.append(value)
        else:
            self.back.append(value)

        self.cur += 1
        return True


    def deleteFront(self) -> bool:
        if self.cur == 0:
            return False

        _ = self.front.pop()
        self.cur -= 1

        if len(self.front) == 0:
            self.front = self.back[::-1]
            self.back = []

        return True


    def deleteLast(self) -> bool:
        if self.cur == 0:
            return False

        if len(self.back) == 0:
            _ = self.front.pop(0)
        else:
            _ = self.back.pop()


        self.cur -= 1
        return True

    def getFront(self) -> int:
        if self.cur == 0:
            return -1

        return self.front[-1]


    def getRear(self) -> int:
        if self.cur == 0:
            return -1

        if len(self.back) == 0:
            return self.front[0]

        return self.back[-1]


    def isEmpty(self) -> bool:
        return self.cur == 0


    def isFull(self) -> bool:
        return self.cur == self.k