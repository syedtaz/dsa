from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

      acc = 0

      for i, row in enumerate(grid):
          for j, v in enumerate(row):
              if v == 0:
                  continue

              if j == 0 or j > 0 and row[j - 1] == 0:
                  acc += 2

              if i == 0 or i > 0 and grid[i - 1][j] == 0:
                  acc += 2

      return acc