import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [float('inf')] * (1 + len(nums))
        dp[0] = -float('inf')
        
        max_slot = 0
        for ix, n in enumerate(nums):
            slot = bisect.bisect_left(dp, n)
            dp[slot] = n
            max_slot = max(max_slot, slot)
        
        return max_slot