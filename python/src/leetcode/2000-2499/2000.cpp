#include "string"
using namespace std;

class Solution {
public:
    string reversePrefix(string word, char ch) {
        size_t index = word.find(ch);
        if (index == string::npos) {
            return word;
        }
        reverse(word.begin(), word.begin() + index + 1);
        return word;
    }
};