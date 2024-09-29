import heapq

type heap_t = tuple[int, int, int]
type price_t = tuple[int, int]


def f(prices: list[list[price_t]]) -> list[tuple[int, int]]:
    def generate_heap(prices: list[list[price_t]]) -> list[heap_t]:
        heap: list[heap_t] = []

        for idx, price_list in enumerate(prices):
            for day, price in price_list:
                heap.append((day, price, idx))

        heapq.heapify(heap)
        return heap

    heap = generate_heap(prices)
    acc: list[price_t] = []
    state = {i: 0 for i in range(len(prices))}

    while len(heap) > 0:
        min_day, price, item = heapq.heappop(heap)
        state[item] = price

        while len(heap) > 0 and heap[0][0] == min_day:
            _, price, item = heapq.heappop(heap)
            state[item] = price

        acc.append((min_day, sum([v for v in state.values()])))

    return acc