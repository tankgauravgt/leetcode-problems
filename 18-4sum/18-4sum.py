class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        
        if len(nums) > 3:
            
            res = []
            for ix1 in range(0, len(nums) - 3, 1):
                if ix1 > 0 and nums[ix1] == nums[ix1 - 1]:
                    continue
                for ix2 in range(ix1 + 1, len(nums) - 2, 1):
                    ix3 = ix2 + 1
                    ix4 = len(nums) - 1
                    while ix4 > ix3:
                        csum = nums[ix1] + nums[ix2] + nums[ix3] + nums[ix4]
                        if csum > target:
                            ix4 = ix4 - 1
                        elif csum < target:
                            ix3 = ix3 + 1
                        else:
                            res = res + [(nums[ix1], nums[ix2], nums[ix3], nums[ix4])]
                            ix3 = ix3 + 1
            
            return sorted(set(res))
        else:
            return []