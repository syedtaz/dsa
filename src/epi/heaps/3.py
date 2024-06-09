from heapq import heappushpop, heapify, heappop


def sort_k_sorted(lst: list[int], k: int) -> list[int]:
    """
    Sorts a k-sorted array.

    A sequence is k-sorted if every element is at most k slots away
    from their position in a sorted list.
    """

    heap: list[int] = lst[:k]
    heapify(heap)

    acc: list[int] = []

    for num in lst[k + 1 :]:
        acc.append(heappushpop(heap, num))

    while len(heap) > 0:
        acc.append(heappop(heap))

    return acc