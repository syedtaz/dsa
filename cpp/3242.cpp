#include <unordered_map>
#include <utility>
#include <vector>

class NeighborSum {
private:
  std::unordered_map<int, std::pair<int, int>> memo;
  std::vector<std::pair<int, int>> adjdelta = {
      {1, 0}, {0, 1}, {-1, 0}, {0, -1}};
  std::vector<std::pair<int, int>> diagdelta = {
      {1, 1}, {-1, 1}, {-1, -1}, {1, -1}};

  bool within_bound(int dx, int dy, int m, int n) {
    return (0 <= dx) && (dx < m) && (0 <= dy) && (dy < n);
  }

public:
  NeighborSum(std::vector<std::vector<int>> &grid) {
    int m = grid.size();
    int n = grid[0].size();

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int adj = 0;
        int diag = 0;

        for (auto p : adjdelta) {
          int dx = i + p.first;
          int dy = j + p.second;

          if (within_bound(dx, dy, m, n)) {
            adj += grid[dx][dy];
          }
        }

        for (auto p : diagdelta) {
          int dx = i + p.first;
          int dy = j + p.second;

          if (within_bound(dx, dy, m, n)) {
            diag += grid[dx][dy];
          }
        }

        memo.insert(std::make_pair(grid[i][j], std::make_pair(adj, diag)));
      }
    }
  }

  int adjacentSum(int value) { return (memo.find(value)->second).first; }

  int diagonalSum(int value) { return (memo.find(value)->second).second; }
};
