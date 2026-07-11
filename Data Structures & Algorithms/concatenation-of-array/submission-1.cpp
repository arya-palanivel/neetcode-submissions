#include <vector>

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> type_shift(nums.size() * 2);
        for (int i = 0; i < nums.size(); ++i){
            type_shift[i] = nums[i];
            type_shift[i+nums.size()] = nums[i];
        }
        return type_shift;
    }
};