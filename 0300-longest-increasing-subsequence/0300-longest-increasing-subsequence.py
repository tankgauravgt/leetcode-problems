class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp = [0] * (1 + len(nums))
        dp[0] = 0
        for ix, n in enumerate(nums):
            cmax = 0
            for jx in range(0, ix):
                if nums[jx] < nums[ix]:
                    cmax = max(cmax, dp[1 + jx])
            dp[1 + ix] = 1 + cmax
        
        return max(dp)