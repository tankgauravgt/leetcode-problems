class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        ex = 0
        ox = 1
        while ex < len(nums) and ox < len(nums):
            if nums[ex] % 2 == 0:
                ex = ex + 2
            else:
                nums[ex], nums[ox] = nums[ox], nums[ex]
                ox = ox + 2
        
        return nums