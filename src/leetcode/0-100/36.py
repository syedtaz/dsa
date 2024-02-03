from typing import List
from itertools import product

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        points = sorted(product([0,1,2], [0,3,6], [3,6,9]), key=lambda x: x[2])

        def valid(x: int, y: int, size: int) -> bool:
            i, j = x, y
            seen : set[str] = set()
            for p in range(size):
                for q in range(size):
                  el = board[i + p][j + q]
                  if not el.isdigit():
                      continue

                  if el in seen:
                      return False
                  seen.add(el)

            return True

        for (x, y, size) in points:
            if not valid(x,y,size):
                return False

        return True

s = Solution()
print(s.isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))