#include <map>
#include <vector>
using namespace std;

class Solution {
    public:
        int findContentChildren(vector<int>& g, vector<int>& s) {
            map<int, int> mappers;
            for (int num: s) mappers[num] += 1;
            int response = 0;
            for (int greed: g) {
                auto it = mappers.lower_bound(greed);
                if (it != mappers.end()) {
                    it->second--;
                    response += 1;
                    if (it->second == 0) mappers.erase(it);
                }
            }
            return response;
        }
};