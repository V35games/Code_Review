#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        for (auto i = 0u; i < nums.size() - 1; i++) {
            for (auto j = 1u + i; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    v.emplace_back(i);
                    v.emplace_back(j);
                    return v;                
                }
            }
        }
        return v;
    }
};