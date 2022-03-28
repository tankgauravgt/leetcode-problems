import bisect

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        if len(nums) < 3:
            return 0
        
        nums = sorted(nums)

        count = 0
        for fx in range(len(nums) - 2):
            lx = fx + 1
            rx = len(nums) - 1
            while lx < rx:
                if nums[lx] + nums[rx] >= target - nums[fx]:
                    rx = rx - 1
                else:
                    count = count + (rx - lx)
                    lx = lx + 1
                    
        return count