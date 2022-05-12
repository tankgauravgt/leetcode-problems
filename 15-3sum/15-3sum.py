class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        
        out = []
        for lx, n in enumerate(nums):
            
            if lx > 0 and nums[lx - 1] == n:
                continue
            
            cx = lx + 1
            rx = len(nums) - 1
            while cx < rx:
                _sum = nums[lx] + nums[cx] + nums[rx]
                if _sum < 0:
                    cx = cx + 1
                elif _sum > 0:
                    rx = rx - 1
                else:
                    out += [(nums[lx], nums[cx], nums[rx])]
                    while cx < rx and nums[cx] == nums[cx + 1]:
                        cx = cx + 1
                    cx = cx + 1
        
        return out