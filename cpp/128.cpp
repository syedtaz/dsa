#include <unordered_set>

inline int streak(const std::unordered_set<int>& set, int number) {
  int acc = 1;

  while (set.contains(number + 1)) {
    acc += 1;
    number += 1;
  }

  return acc;
}

class Solution {
public:
  int longestConsecutive(std::vector<int> &nums) {

    std::unordered_set<int> set = std::unordered_set<int>(nums.begin(), nums.end());
    int acc = 0;

    for (const int num : set) {
      if (!set.contains(num - 1)) {
        acc = std::max(acc, streak(set, num));
      }
    }

    return acc;
  }
};