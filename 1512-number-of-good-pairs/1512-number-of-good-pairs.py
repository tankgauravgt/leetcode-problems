class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        rec = {}
        counter = 0
        for ix, n in enumerate(nums):
            if n in rec:
                counter += rec[n]
                rec[n] += 1
            else:
                rec[n] = 1
        
        return counter