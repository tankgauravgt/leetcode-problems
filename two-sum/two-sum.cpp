class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        
        // creating a set of complements:
        std::map<int, int> comp;
        for (int ix=0; ix<nums.size(); ix++) {
            comp.insert(std::pair<int, int>(nums[ix], ix));
        }
        
        // iterate over all elements and find if there exists a complement:
        for (int ix=0; ix<nums.size(); ix++) {
            if (comp.find(target - nums[ix]) != comp.end()) {
                if (ix != comp[target - nums[ix]]) {
                    return std::vector<int>({ix, comp[target - nums[ix]]});
                }
            }
        }
        
        return std::vector<int>({-1, -1});
    }
};
