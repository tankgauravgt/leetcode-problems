from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        rec = dict(Counter(s))
        
        for c in t:
            if c not in rec.keys():
                return False
            else:
                if rec[c] == 1:
                    rec.pop(c)
                else:
                    rec[c] = rec[c] - 1
        
        return len(rec) == 0