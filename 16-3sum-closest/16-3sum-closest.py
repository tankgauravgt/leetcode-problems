class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        diff = float('inf')
        nums = sorted(nums)
        
        for fx in range(len(nums) - 2):
            
            lx = fx + 1
            rx = len(nums) - 1
            
            while lx < rx:
                
                # calculate sum:
                isum = nums[fx] + nums[lx] + nums[rx]
                
                # check if absolute difference is less:
                if abs(target - isum) < abs(diff):
                    diff = target - isum
                    
                # move pointers based on current sum:
                if isum < target:
                    lx = lx + 1
                else:
                    rx = rx - 1
                    
                # if difference is zero, return value:
                if diff == 0:
                    break
                
        return target - diff