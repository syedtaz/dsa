from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        avail_rows, avail_cols = [True] * n, [True] * n
        acc, nrows, ncols = 0, n, n
        i = len(queries) - 1

        while i >= 0 and (nrows + ncols > 0):
            t, idx, val = queries[i][0], queries[i][1], queries[i][2]
            if t == 0 and avail_rows[idx]:
                acc += ncols * val
                avail_rows[idx] = False
                nrows -= 1
            elif t == 1 and avail_cols[idx]:
                acc += nrows * val
                avail_cols[idx] = False
                ncols -= 1

            i -= 1

        return acc
