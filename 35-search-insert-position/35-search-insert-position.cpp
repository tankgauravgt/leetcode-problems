class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return (int) std::distance(nums.begin(), std::lower_bound(nums.begin(), nums.end(), target));
    }
};
