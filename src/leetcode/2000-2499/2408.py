from typing import List
from collections import defaultdict


class SQL:
    ids: dict[str, int]
    state: dict[str, defaultdict[int, list[str]]]

    def __init__(self, names: List[str], columns: List[int]) -> None:
        self.ids = {name: 1 for name in names}
        self.state = {name: defaultdict(list[str]) for name in names}

    def insertRow(self, name: str, row: List[str]) -> None:
        id = self.ids[name]
        self.state[name][id] = row
        self.ids[name] += 1
        return None

    def deleteRow(self, name: str, rowId: int) -> None:
        _ = self.state[name].pop(rowId)
        return None

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.state[name][rowId][columnId]
