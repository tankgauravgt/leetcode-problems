class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        lx = 0
        res = 0
        prod = 1
        for rx in range(len(nums)):
            prod = prod * nums[rx]
            while lx <= rx and prod >= k:
                prod = prod / nums[lx]
                lx = lx + 1
            res += (rx - lx + 1)
        
            # print(nums, k, nums[lx:rx+1])
        
        return res