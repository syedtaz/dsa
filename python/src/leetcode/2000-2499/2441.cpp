#include "vector";
#include "set";
#include "ranges";
using namespace std;

class Solution {
public:
    int findMaxK(vector<int>& nums) {
        auto s = set(nums.begin(), nums.end());
        auto filtered = s | views::filter([&s](int i) { return s.contains(-i);});
        return filtered.empty() ? -1 : *ranges::rbegin(filtered);
    }
};