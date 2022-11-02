import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float('inf')] * (1 + len(nums))
        dp[0] = -float('inf')
        cmax = 0
        for ix, n in enumerate(nums):
            jx = bisect.bisect_left(dp, n)
            dp[jx] = n
            cmax = max(cmax, jx)
        return cmax