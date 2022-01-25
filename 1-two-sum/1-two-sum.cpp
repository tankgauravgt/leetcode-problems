class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // creating complement dictionary:
        std::unordered_map<int, int> rec;
        
        // filling the complement dictionary:
        for (int ix = 0; ix < nums.size(); ix++)
            rec[target - nums[ix]] = ix;
        
        // search if complement exist and index is different:
        for (int ix = 0; ix < nums.size(); ix++) {
            if (rec.count(nums[ix]) > 0) {
                if (ix != rec[nums[ix]]) {
                    return std::vector<int>({ix, rec[nums[ix]]});
                }
            }
        }
        
        // return empty vector if solution does not exist:
        return std::vector<int>();
    }
};
