class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        rec = {}
        counter = 0
        for ix, n in enumerate(nums):
            if n in rec:
                counter += len(rec[n])
                rec[n] += [ix]
            else:
                rec[n] = [ix]
        
        return counter