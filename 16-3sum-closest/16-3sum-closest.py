class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        cmin = float('inf')
        nums = sorted(nums)
        
        for fx in range(len(nums) - 2):
            
            lx = fx + 1
            rx = len(nums) - 1
            
            while lx < rx:
                
                # calculate sum:
                isum = nums[fx] + nums[lx] + nums[rx]
                
                if abs(target - isum) < abs(cmin):
                    cmin = target - isum
                    
                if isum < target:
                    lx = lx + 1
                else:
                    rx = rx - 1
                    
                if cmin == 0:
                    break
                    
        return target - cmin