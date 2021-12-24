class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # creating dictionary with complements:
        complements = {num: ix for ix, num in enumerate(nums)}
        
        # if complemented number is found in dictionary and is different, return pair:
        for ix, num in enumerate(nums):
            if (target - num) in complements.keys() and ix != complements[target - num]:
                return [ix, complements[target - num]]