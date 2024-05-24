from typing import Optional

# Collision resolution using chaining.


class List:
    val: int
    next: "Optional[List]"
    prev: "Optional[List]"

    def __init__(
        self, val: int, next: "Optional[List]", prev: "Optional[List]"
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev


L = Optional[List]


def search(lst: L, v: int) -> L:
    return None if lst is None else (lst if lst.val == v else search(lst.next, v))


def delete(lst: L, v: int) -> None:
    if lst is None:
        return None

    if lst.val == v:
        match (lst.prev, lst.next):
            case (None, None):
                pass
            case (None, next):
                assert next is not None
                next.prev = None
            case (prev, None):
                assert prev is not None
                prev.next = None
            case (prev, next):
                assert prev is not None and next is not None
                next.prev = prev
                prev.next = next
        del lst
        return None

    return None if lst.next is None else delete(lst.next, v)


class MyHashSet:
    t: list[Optional[List]]
    size: int

    def __init__(self):
        self.size = 1024
        self.t = [None] * self.size

    def hash(self, value: int) -> int:
        return value % self.size

    def add(self, key: int) -> None:
        idx = self.hash(key)
        if self.t[idx] is None:
            self.t[idx] = List(val=key, next=None, prev=None)
            return None

        head = self.t[idx]
        assert head is not None

        if search(head, key) is None:
            x = List(val=key, next=head, prev=None)
            head.prev = x
            self.t[idx] = x

        return None

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        if self.t[idx] is None:
            return None

        node = self.t[idx]
        assert node is not None

        if node.val == key:
            self.t[idx] = node.next
            return None

        delete(node, key)
        return None

    def contains(self, key: int) -> bool:
        return search(self.t[self.hash(key)], key) is not None


# class MyHashSet:
#     t : list[int | None]
#     size : int

#     def __init__(self):
#         self.size = 2
#         self.t = [None] * self.size

#     def hash(self, v: int) -> int:
#         return v % self.size

#     def rebalance(self) -> None:
#         self.size = 2 ** (int(math.log2(self.size)) + 1)
#         new_t = [None] * self.size

#         for v in filter(lambda x: x is not None, self.t):
#             new_t[self.hash(v)] = v # type: ignore

#         self.t = new_t
#         return None

#     def search(self, idx: int, v: int) -> tuple[bool, int]:
#         cur = idx

#         while cur < self.size and self.t[cur] != v:
#             cur += 1

#         return (False, cur) if (cur > self.size or self.t[cur] != v) else (True, cur)

#     def add(self, key: int) -> None:
#         idx = self.hash(key)
#         if self.t[idx] is None:
#             self.t[idx] = key
#             return

#         cur = idx
#         while  and self.t[cur] is not None:
#             cur += 1

#         if cur == self.size:
#             self.rebalance()
#             self.add(key)
#         else:
#             self.t[cur] = key
#             return


#     def remove(self, key: int) -> None:
#         idx = self.hash(key)
#         if self.t[idx] is None:
#             return None

#         found, nidx = self.search(idx, key)
#         if not found:
#             return None

#         self.t[nidx] = None
#         return None


#     def contains(self, key: int) -> bool:
#         idx = self.hash(key)
#         if self.t[idx] is None:
#             return False
#         v, _ = self.search(idx, key)
#         return v
