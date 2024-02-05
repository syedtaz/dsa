from typing import List
from array import array

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        static = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        rows = array('H', static)
        cols = array('H', static)
        boxes = array('H', static)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                v = int(board[row][col]) - 1

                if rows[row] & (1 << v):
                    return False

                if cols[col] & (1 << v):
                    return False

                rows[row] |= (1 << v)
                cols[col] |= (1 << v)

                idx = 3 * (row // 3) + col // 3
                if boxes[idx] & (1 << v):
                    return False

                boxes[idx] |= (1 << v)

        return True