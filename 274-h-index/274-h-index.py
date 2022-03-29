class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations = sorted(citations, reverse=True)
        
        print(citations)
        
        counter = 0
        for ix, c in enumerate(citations):
            if (ix + 1) <= c:
                counter += 1
        
        return counter