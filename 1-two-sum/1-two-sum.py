class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comp = {}
        for ix, n in enumerate(nums):
            if n not in comp:
                comp[target - n] = ix
            else:
                return [comp[n], ix]