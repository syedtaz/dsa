from typing import Optional

class Node:
    key: int
    value: int
    next: Optional["Node"]
    prev: Optional["Node"]

    def __init__(
        self, key: int, value: int, next: Optional["Node"], prev: Optional["Node"]
    ) -> None:
        self.key, self.value, self.next, self.prev = key, value, next, prev

    def __repr__(self) -> str:
        return f"{self.value}"

class LRUCache:
    capacity: int
    size: int
    head: Optional["Node"]
    tail: Optional["Node"]
    table : dict[int, Node]

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.table = {}

    def mut_head(self, node: Node) -> None:
        assert self.head is not None
        temp = self.head
        temp.prev = node
        self.head = node
        node.prev = None
        node.next = temp
        return

    def splice(self, key: int) -> None:
        assert self.head is not None and self.tail is not None
        node = self.table[key]

        if self.head == node:
            return

        if self.tail == node:
            assert node.prev is not None
            prev = node.prev
            self.tail = prev

        if node.next is not None:
          node.next.prev = node.prev
        if node.prev is not None:
          node.prev.next = node.next
        self.mut_head(node)
        return

    def get(self, key: int) -> int:
        if self.size == 0 or key not in self.table:
            return -1

        self.splice(key)
        return self.table[key].value

    def put(self, key: int, value: int) -> None:
        if self.head is None and self.tail is None:
            node = Node(key, value, None, None)
            self.head = node
            self.tail = node
            self.table[key] = node
            self.size = 1
            return

        if key in self.table:
            self.table[key].value = value
            self.splice(key)
            return

        node = Node(key, value, None, None)
        self.size += 1

        if self.size > self.capacity:
            tail = self.tail
            assert tail is not None
            self.size -= 1

            if tail.prev is None: # capacity is 1
                assert self.head == tail
                self.table.pop(tail.key)
                self.table[node.key] = node
                self.head = node
                self.tail = node
                return
            else:
                self.tail = tail.prev
                self.table.pop(tail.key)

        self.mut_head(node)
        self.table[node.key] = node
        return