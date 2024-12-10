import abc
from abc import ABC, abstractmethod
from typing import List, Callable
from dataclasses import dataclass


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


f = Callable[[int, int], int]

add: f = lambda x, y: x + y
sub: f = lambda x, y: x - y
mul: f = lambda x, y: x * y
div: f = lambda x, y: int(x / y)
operators = {"+": add, "-": sub, "*": mul, "/": div}


@dataclass
class TNode(Node):
    operation: f
    left: "Node"
    right: "Node"

    def evaluate(self) -> int:
        lv = self.left.evaluate()
        rv = self.right.evaluate()
        return self.operation(lv, rv)


@dataclass
class ConstNode(Node):
    value: int

    def evaluate(self) -> int:
        return self.value


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> "Node":
        stack: list[Node] = []

        for ch in postfix:
            if ch in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(TNode(operators[ch], left, right))
            else:
                stack.append(ConstNode(int(ch)))

        assert len(stack) == 1
        return stack.pop()