# 3.11 Design a dictionary data structure in which search, insertion, and
# deletion can all be processed in O(1) time in the worst case. You may assume
# the set elements are integers drawn from a finite set 1, 2, .., n, and
# initialization can take O(n) time.

class ConstDict:
  store: list[bool]

  def __init__(self, n : int):
    self.store = [False] * n

  def __str__(self) -> str:
    return str(self.store)

  def search(self, k: int) -> int | None:
    return k if self.store[k] else None

  def insert(self, k: int) -> None:
    self.store[k] = True

  def delete(self, k: int) -> None:
    self.store[k] = False