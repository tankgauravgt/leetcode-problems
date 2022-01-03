class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        lx = 0
        rx = 0
        csum = nums[0]
        min_len = float('inf')
        
        # checking min_len using windowing method:
        while rx >= lx and rx < len(nums) - 1:
            if csum < target:
                rx = rx + 1
                csum = csum + nums[rx]
            else:
                csum = csum - nums[lx]
                min_len = min(min_len, rx - lx + 1)
                lx = lx + 1
        
        # checking if last window can further be minimized:
        while target <= csum:
            csum = csum - nums[lx]
            min_len = min(min_len, rx - lx + 1)
            lx = lx + 1
        
        return 0 if min_len == float('inf') else min_len