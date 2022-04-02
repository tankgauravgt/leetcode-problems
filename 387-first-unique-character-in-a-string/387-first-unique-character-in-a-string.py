from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        rec = dict(Counter(s))
        
        for ix, c in enumerate(s):
            if rec[c] < 2:
                return ix
        return -1