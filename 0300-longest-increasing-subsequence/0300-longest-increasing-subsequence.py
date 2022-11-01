class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        def lis(ex, memo):
            if ex == 0:
                return 1
            if memo[ex] != -1:
                return memo[ex]
            cmax = 1
            for sx in range(ex):
                pmax = lis(sx, memo)
                if nums[ex] <= nums[sx]:
                    continue
                cmax = max(cmax, 1 + pmax)
            memo[ex] = cmax
            return cmax

        memo = [-1] * len(nums)
        memo[0] = 1
        
        res = lis(len(nums) - 1, memo)
        return max(memo)