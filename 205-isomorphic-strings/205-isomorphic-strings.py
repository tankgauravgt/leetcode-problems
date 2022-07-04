class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        rec1 = {}
        rec2 = {}
        
        for c1, c2 in zip(s, t):
            if c1 not in rec1:
                rec1[c1] = c2
            if c2 not in rec2:
                rec2[c2] = c1
        
        for c1, c2 in zip(s, t):
            if rec1[c1] != c2 or rec2[c2] != c1:
                return False
        
        return True