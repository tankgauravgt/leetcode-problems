class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cmax = csum = nums[0]
        for n in nums[1::]:
            csum = max(n, csum + n)
            cmax = max(csum, cmax)
        return cmax