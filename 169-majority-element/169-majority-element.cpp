class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int cnt = 0;
        int last = 0;
        for (int ix = 0; ix < nums.size(); ix++) {
            if (cnt == 0)
                last = nums[ix];
            if (nums[ix] == last)
                cnt++;
            else
                cnt--;
        }
        return last;
    }
};