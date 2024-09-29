#include <string>

class Solution {
public:
  int scoreOfString(std::string s) {
    int length = s.length();
    int acc = 0;

    for (int i = 0; i < length - 1; i++) {
      acc += abs(((int)s[i]) - ((int)s[i + 1]));
    }

    return acc;
  }
};