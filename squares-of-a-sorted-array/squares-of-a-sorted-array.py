class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        lx = 0
        rx = len(nums) - 1
        
        res = []
        while rx >= lx:
            if (nums[lx] ** 2) >= (nums[rx] ** 2):
                res.append(nums[lx] ** 2)
                lx = lx + 1
            else:
                res.append(nums[rx] ** 2)
                rx = rx - 1
        
        return res[::-1]