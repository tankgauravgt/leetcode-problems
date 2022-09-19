class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        rec = set()
        for n in nums:
            if n in rec:
                return n
            rec.add(n)
        
        return -1