from typing import List
from collections import deque

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        acc : list[int] = [kill]
        queue : deque[int] = deque([kill])
        seen : set[int] = set()

        while len(queue) > 0:
            print(queue)
            cur = queue.popleft()
            if cur == 0:
                return pid

            for i, cand in enumerate(ppid):
                if cand == cur and cand not in seen:
                    acc.append(pid[i])
                    queue.append(cand)

            seen.add(cur)

        return acc

s = Solution()
print(s.killProcess(pid=[1,2,3], ppid=[0,1,2], kill=1))