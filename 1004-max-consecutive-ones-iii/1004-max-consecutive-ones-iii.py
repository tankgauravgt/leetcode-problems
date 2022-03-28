class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        lx = 0
        rx = 0
        cmax = 0
        
        rec = {
            0: 0, 
            1: 0
        }
        
        cost = 0
        while lx <= rx and rx < len(nums):
            if cost <= k:
                rec[nums[rx]] += 1
                rx = rx + 1
                cost = (rx - lx) - rec[1]
            else:
                rec[nums[lx]] -= 1
                lx = lx + 1
                cost = (rx - lx) - rec[1]
            
            if cost <= k:
                cmax = max(cmax, rx - lx)
            
            # print(lx, rx, nums[lx:rx], cost)
        
        return cmax