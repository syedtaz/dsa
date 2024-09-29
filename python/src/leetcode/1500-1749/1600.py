from collections import defaultdict
from typing import List


class ThroneInheritance:
    king: str
    children: dict[str, list[str]]
    dead: set[str]

    def __init__(self, kingName: str) -> None:
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.children[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        acc: list[str] = []
        stack: list[str] = [self.king]

        while stack:
            person = stack.pop()
            if person not in self.dead:
                acc.append(person)
            for child in self.children[person][::-1]:
                stack.append(child)

        return acc
