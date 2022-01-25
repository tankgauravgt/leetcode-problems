class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // creating complement dictionary:
        std::unordered_map<int, int> rec;
        
        // filling the complement dictionary:
        for (int ix = 0; ix < nums.size(); ix++) {
            if (rec.count(nums[ix]) > 0) {
                return std::vector<int>({ix, rec[nums[ix]]});
            }
            rec[target - nums[ix]] = ix;
        }
        
        // return empty vector if solution does not exist:
        return std::vector<int>();
    }
};
