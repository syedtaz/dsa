from typing import List


class IDAlloc:
    next: int
    allocated: set[int]

    def __init__(self):
        self.next = 1
        self.allocated = set()

    def request(self) -> int:
        temp = self.next
        nnext = self.next + 1

        while nnext in self.allocated:
            nnext += 1

        self.next = nnext
        self.allocated.add(temp)
        return temp

    def remove(self, id: int) -> None:
        self.allocated.remove(id)
        if id < self.next:
            self.next = id


class FileSharing:
    chunks: dict[int, set[int]]
    alloc: IDAlloc

    def __init__(self, m: int):
        self.chunks = {x: set() for x in range(1,m + 1)}
        self.alloc = IDAlloc()

    def join(self, ownedChunks: List[int]) -> int:
        id = self.alloc.request()

        for chunk in ownedChunks:
            self.chunks[chunk].add(id)

        return id

    def leave(self, userID: int) -> None:

        for chunk in self.chunks.values():
            if userID in chunk:
                chunk.remove(userID)

        self.alloc.remove(userID)
        return

    def request(self, userID: int, chunkID: int) -> List[int]:
        if chunkID not in self.chunks:
            return []

        ids = list(self.chunks[chunkID])
        if len(ids) == 0:
            return []

        self.chunks[chunkID].add(userID)
        return ids