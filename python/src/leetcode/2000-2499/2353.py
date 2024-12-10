from typing import List
from collections import defaultdict


class Node:
    prev: "Node | None"
    next: "Node | None"
    name: str
    rating: int

    def __init__(
        self, rating: int, name: str, prev: "Node | None", next: "Node | None"
    ) -> None:
        self.prev = prev
        self.next = next
        self.name = name
        self.rating = rating

    def balance(self) -> None:


        while self.prev is not None and self.prev.rating <= self.rating:

            if self.prev.rating == self.rating and self.prev.name <= self.name:
                break

            temp = self.prev
            self.prev = temp.prev
            temp.next = self.next
            temp.prev = self
            self.next = temp

        if self.prev is None:
            return self

        return None

    # def __repr__(self) -> str:
    #     return f"({self.name} . {self.rating})" + " --> " + (self.next.__repr__() if self.next is not None else "None")


class Cuisine:
    head: Node
    mapping: dict[str, Node]

    def __init__(self, foods: list[tuple[str, int]]) -> None:
        foods.sort(key=lambda x: x[1])
        curr = None
        mapping = {}

        for food, rating in foods:
            node = Node(rating, food, None, curr)
            mapping[food] = node
            curr = node

        assert curr is not None
        self.head = curr
        self.mapping = mapping

    def change(self, food: str, rating: int) -> None:
        node = self.mapping[food]
        node.rating = rating
        if (newhead := node.balance()) is not None:
            self.head = newhead

    def hd(self) -> str:
        return self.head.name


class FoodRatings:
    cuisines: dict[str, Cuisine]

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        csmap: dict[str, list[tuple[str, int]]] = defaultdict(list)

        for fd, cs, rt in zip(foods, cuisines, ratings):
            csmap[cs].append((fd, rt))

        converted = {name: Cuisine(lst) for name, lst in csmap.items()}
        self.cuisines = converted

    def changeRating(self, food: str, newRating: int) -> None:

        for cuisine in self.cuisines.values():
            if food in cuisine.mapping:
                cuisine.change(food, newRating)
                break

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine].head.name
