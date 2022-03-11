class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        diff = float('inf')
        nums = sorted(nums)
        for ix in range(len(nums) - k + 1):
            arr = nums[ix:ix+k]
            if (arr[k-1] - arr[0]) < diff:
                diff = arr[k-1] - arr[0]
        
        return diff