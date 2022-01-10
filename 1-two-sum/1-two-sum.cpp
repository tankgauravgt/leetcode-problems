class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // creating complement dictionary:
        std::map<int, int> rec;
        
        // filling the complement dictionary:
        for (int ix = 0; ix < nums.size(); ix++)
            rec.insert(std::pair<int, int>(target - nums[ix], ix));
        
        // search if complement exist and index is different:
        for (int ix = 0; ix < nums.size(); ix++) {
            if (rec.find(nums[ix]) != rec.end()) {
                if (ix != rec[nums[ix]]) {
                    return std::vector<int>({ix, rec[nums[ix]]});
                }
            }
        }
        
        // return empty vector if solution does not exist:
        return std::vector<int>();
    }
};
