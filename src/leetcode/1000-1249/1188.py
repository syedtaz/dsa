from threading import Lock, Event
from collections import deque

class BoundedBlockingQueue(object):
    _mutation_lock: Lock
    _size_lock: Lock
    n: int
    cap: int
    queue: deque[int]
    _not_at_cap: Event
    _not_at_zero: Event


    def __init__(self, capacity: int) -> None:
        self._mutation_lock = Lock()
        self._size_lock = Lock()
        self.n = 0
        self.cap = capacity
        self.queue = deque([])
        self._not_at_cap = Event()
        self._not_at_cap.set()
        self._not_at_zero = Event()

    def enqueue(self, element: int) -> None:
        self._not_at_cap.wait()

        with self._mutation_lock:
            self.queue.append(element)

            if len(self.queue) == self.cap:
                self._not_at_cap.clear()

            if not self._not_at_zero.is_set():
                self._not_at_zero.set()

        return


    def dequeue(self) -> int:
        self._not_at_zero.wait()

        with self._mutation_lock:
            item = self.queue.popleft()

            if not self._not_at_cap.is_set():
                self._not_at_cap.set()

            if len(self.queue) == 0:
                self._not_at_zero.set()

            return item


    def size(self) -> int:
        with self._size_lock:
            return self.n