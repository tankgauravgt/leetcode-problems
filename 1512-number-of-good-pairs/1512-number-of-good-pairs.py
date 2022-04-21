class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        rec = {}
        counter = 0
        for ix, n in enumerate(nums):
            if n in rec:
                for i in rec[n]:
                    if ix > i:
                        counter += 1
                rec[n] += [ix]
            else:
                rec[n] = [ix]
        
        return counter