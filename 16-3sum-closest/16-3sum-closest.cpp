class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        std::sort(nums.begin(), nums.end());
        
        int cx, rx, s;
        int d = INT_MAX;
        
        for(int lx=0; lx < nums.size() - 2; lx++) {
            
            cx = 1 + lx;
            rx = nums.size() - 1;
            
            while (cx < rx) {
                s = nums[lx] + nums[cx] + nums[rx];
                if (std::abs(target - s) < std::abs(d)) {
                    d = target - s;
                }
                if (target == s) {
                    return s;
                }
                if (s < target) {
                    cx = cx + 1;
                } else {
                    rx = rx - 1;
                }
            }
            
        }
        
        return target - d;
    }
};