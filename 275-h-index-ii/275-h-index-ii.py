import bisect

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        count = 0
        for ix, c in enumerate(citations[::-1]):
            if (ix + 1) <= c:
                count += 1
        
        return count