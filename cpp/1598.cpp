#include <string>

class Solution {
public:
  int minOperations(std::vector<std::string> &logs) {
    int acc = 0;

    for (auto op : logs) {
      if ((op == "../")) {
        if (acc > 0) {
          acc -= 1;
        }

      } else if (op == "./") {
        continue;
      } else {
        acc += 1;
      }
    }

    return acc;
  }
};