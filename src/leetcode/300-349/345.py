from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:

        queue: deque[int] = deque(
            [idx for idx, ch in enumerate(s) if ch.lower() in {"a", "e", "i", "o", "u"}]
        )

        copy = [x for x in s]

        while len(queue) > 1:
            left, right = queue.popleft(), queue.pop()
            copy[left], copy[right] = copy[right], copy[left]

        return "".join(copy)
