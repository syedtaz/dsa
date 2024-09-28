#include <string>
#include <unordered_map>

class OrderedStream {
private:
  int N;
  int pos;
  std::unordered_map<int, std::string> nodes;

  std::vector<std::string> flush() {
    std::vector<std::string> acc;

    while (nodes.contains(pos) && (pos <= N)) {
      acc.push_back(nodes.find(pos)->second);
      nodes.erase(pos);
      pos += 1;
    }

    return acc;
  }

public:
  OrderedStream(int n) : N(n), pos(1) {}

  std::vector<std::string> insert(int idKey, std::string value) {
    nodes.insert(std::make_pair(idKey, value));
    return flush();
  }
};