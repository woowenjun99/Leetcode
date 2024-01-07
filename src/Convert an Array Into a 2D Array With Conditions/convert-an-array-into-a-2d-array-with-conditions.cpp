#include <vector>
using namespace std;

class Solution {
    public:
        vector<vector<int>> findMatrix(vector<int>& nums) {
            unordered_map<int, int> mappers;
            for (int num: nums) mappers[num]++;
            vector<vector<int>> solution;
            int count = 0;
            while (count < nums.size()) {
                vector<int> row;
                for (auto it = mappers.begin(); it != mappers.end(); ++it) {
                    if (it->second > 0) {
                        row.push_back(it->first);
                        it->second -= 1;
                        count++;
                    }
                }
                solution.push_back(row);
            }
            return solution;
        }
};