from collections import Counter

class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        rec = dict(Counter(arr))
        
        out = 0
        for k, v in rec.items():
            if (k + 1) in rec.keys():
                out += rec[k]
        
        return out