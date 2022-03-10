from collections import Counter

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        count = 0
        for ix in range(0, len(s) - 2, 1):
            if len(set(s[ix:ix + 3])) == 3:
                count += 1
        
        return count