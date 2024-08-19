#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
      std::unordered_map<int, int> map;
      map.reserve(nums.size());
      std::vector<int> result;

      int index = -1;
      for (auto el : nums) {
        index += 1;

        if (auto map_idx = map.find(target - el); map_idx != map.end()) {
          result.push_back(index);
          result.push_back(map_idx->second);
          return result;
        }

        map.insert({el, index});
      }

      return result;
    }
};