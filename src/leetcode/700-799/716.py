from typing import NamedTuple

Item = NamedTuple("Item", [("value", int), ("max", int)])


class MaxStack:
    stack: list[Item]

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(Item(value=x, max=x))
            return

        curr_max = self.stack[-1].max
        item = Item(value=x, max=max(curr_max, x))
        self.stack.append(item)

    def pop(self) -> int:
        return self.stack.pop().value

    def top(self) -> int:
        return self.stack[-1].value

    def peekMax(self) -> int:
        return self.stack[-1].max

    def popMax(self) -> int:
        return self.stack.pop().max

s = MaxStack()
s.push(5)
s.push(1)
print(s.popMax())
print(s.peekMax())