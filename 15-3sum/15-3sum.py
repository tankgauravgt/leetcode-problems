class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        
        out = []
        for lx, n in enumerate(nums):
            
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
                    cx = cx + 1
        
        return set(out)