class Solution:
        
    def search(self, nums: List[int], target: int) -> int:
        
        sx = 0
        ex = len(nums) - 1
        
        while sx <= ex:
            
            mx = sx + ((ex - sx) // 2)
            if nums[mx] == target:
                return mx       
            
            if nums[sx] < nums[mx]:
                if target < nums[sx] or target > nums[mx]:
                    sx = mx + 1
                else:
                    ex = mx - 1
            elif nums[sx] > nums[mx]:
                if target > nums[ex] or target < nums[mx]:
                    ex = mx - 1
                else:
                    sx = mx + 1
            else:
                sx = sx + 1
            
        return -1