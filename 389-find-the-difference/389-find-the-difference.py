from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        rec1 = Counter(t)
        rec2 = Counter(s)
        
        for k, v in rec2.items():
            if rec1[k] != v:
                return k
            else:
                rec1.pop(k)
        
        return list(rec1.keys())[0]