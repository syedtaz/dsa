def binary_search(low: int, high: int, arr: list[tuple[str, int]], target: int) -> int:
    if low > high:
        return high if arr[high][1] <= target else low

    mid = low + (high - low) // 2
    _, v = arr[mid]

    if v == target:
        return mid
    elif v < target:
        return binary_search(mid + 1, high, arr, target)
    else:
        return binary_search(low, mid - 1, arr, target)


from collections import defaultdict


class TimeMap:
    map: dict[str, list[tuple[str, int]]]

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        return None

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map[key]
        if len(lst) == 0:
            return ""

        idx = binary_search(0, len(lst) - 1, lst, timestamp)
        return "" if self.map[key][idx][1] > timestamp else self.map[key][idx][0]

# M = TimeMap()
# M.set("a", "bar", 1)
# M.set("x", "b", 3)
# print(M.get("b", 3))
# M.set("foo", "bar2", 4)
# print(M.get("foo", 4))
# print(M.get("foo", 5))