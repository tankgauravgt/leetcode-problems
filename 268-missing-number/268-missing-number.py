class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = len(nums)
        for ix, n in enumerate(nums):
            out = out ^ (n ^ ix)
        return out