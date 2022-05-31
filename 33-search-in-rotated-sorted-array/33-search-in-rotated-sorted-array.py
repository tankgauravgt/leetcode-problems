class Solution:
    
    def binSearchRotated(self, arr, target, sx, ex):

        while sx <= ex:
            
            mx = sx + ((ex - sx) // 2)
            if arr[mx] == target:
                return mx
            
            
            if arr[sx] < arr[mx]:
                if target < arr[sx] or target > arr[mx]:
                    sx = mx + 1
                else:
                    ex = mx - 1
            elif arr[sx] > arr[mx]:
                if target > arr[ex] or target < arr[mx]:
                    ex = mx - 1
                else:
                    sx = mx + 1
            else:
                sx = sx + 1
            
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearchRotated(nums, target, 0, len(nums) - 1)
        
#         0 1 2 3 4 5 6
#         4 5 6 7 0 1 2 | 0
#         s     m     e