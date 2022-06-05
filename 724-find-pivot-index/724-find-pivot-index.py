class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        lsum = 0
        rsum = sum(nums) - nums[0]
        for lx, n in enumerate(nums):
            if (rsum == lsum):
                return lx
            else:
                if lx < len(nums) - 1:
                    rsum = rsum - nums[lx + 1]
                lsum = lsum + n
        return -1