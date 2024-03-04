from typing import List
from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        queue : deque[int] = deque(tokens)
        cur_score, cur_power = 0, power
        max_score = 0

        while len(queue) > 0:
            if cur_power >= queue[0]:
                cur_power -= queue.popleft()
                cur_score += 1
                max_score = max(max_score, cur_score)
                continue

            if cur_score >= 1:
                cur_score -= 1
                cur_power += queue.pop()
                continue

            break

        return max_score