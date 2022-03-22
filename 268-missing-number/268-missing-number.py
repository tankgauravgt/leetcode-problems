class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        rec = set(nums)
        
        for n in range(len(nums)+1):
            if n not in rec:
                return n