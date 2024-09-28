#include <unordered_map>
#include <vector>

struct Position {
  int x;
  int y;

  bool operator==(Position const &) const = default;
};

class UnionFind {
private:
  std::unordered_map<Position, Position> parents;
  std::unordered_map<Position, int> ranks;

  Position find(Position node) {
    auto result = parents.find(node);
    if (result->second != node) {
      parents.insert_or_assign(node, find(result->second));
    }

    return parents.find(node)->second;
  }

public:
  UnionFind(const int m, const int n) {
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        parents.insert(Position{i, j}, Position{i, j});
        ranks.insert({Position{.x = i, .y = j}, 0});
      }
    }
  }

  void Union(Position x, Position y) {
    Position xbar = find(x);
    Position ybar = find(y);

    if (xbar == ybar) {
      return;
    }

    int xbar_rank = ranks.find(xbar)->second;
    int ybar_rank = ranks.find(ybar)->second;

    if (xbar_rank > ybar_rank) {
      parents.insert(ybar, xbar);
    } else {
      parents.insert(xbar, ybar);
      if (xbar_rank == ybar_rank) {
        ranks.find(ybar)->second += 1;
      }
    }
  }

  std::vector<Position> get_surrounded() {
    std::unordered_map<Position, std::vector<Position>> sets;

    for (auto pairs : parents) {
      if (pairs.first != pairs.second) {
        auto lst = sets.emplace(s)
      }
    }
  }
};

class Solution {
private:
  std::vector<Position> neighbors;

  void update_neighbors(const int x, const int y, const int m, const int n) {
    neighbors.clear();
    if (x + 1 < m) {
      neighbors.push_back(Position{x + 1, y});
    }
    if (x - 1 >= 0) {
      neighbors.push_back(Position{x - 1, y});
    }
    if (y + 1 < n) {
      neighbors.push_back(Position{x, y + 1});
    }
    if (y - 1 >= 0) {
      neighbors.push_back(Position{x, y - 1});
    }
  }

  void update_regions(UnionFind &uf, std::vector<std::vector<char>> &board) {
    const int m = board.size();
    const int n = board[0].size();

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (board[i][j] == 'X') {
          continue;
        }

        Position pos = Position{i, j};
        update_neighbors(i, j, m, n);
        for (auto neighbor : neighbors) {
          if (board[neighbor.x][neighbor.y] == 'O') {
            uf.Union(pos, neighbor);
          }
        }
      }
    }
  }

public:
  void solve(std::vector<std::vector<char>> &board) {
    const int m = board.size();
    const int n = board[0].size();
    UnionFind uf = UnionFind(m, n);
    update_regions(uf, board);
  }
};