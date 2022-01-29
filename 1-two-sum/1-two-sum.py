class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for ix, n in enumerate(nums):
            if n in comp.keys():
                return [ix, comp[n]]
            comp[target - n] = ix
        return []