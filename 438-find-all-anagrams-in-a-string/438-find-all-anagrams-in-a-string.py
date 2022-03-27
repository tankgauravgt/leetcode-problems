class Solution:
    
    def __init__(self):
        self.rec1 = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        self.rec2 = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    
    
    def compare_dict(self, d1, d2):
        for k in d1:
            if d1[k] != d2[k]:
                return False
        return True
    
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        for c in p:
            self.rec2[c] += 1
        
        for c in s[0:len(p)]:
            self.rec1[c] += 1
        
        out = []
        if self.compare_dict(self.rec1, self.rec2):
            out += [0]
        
        for sx in range(len(p), len(s)):
            self.rec1[s[sx - len(p)]] -= 1
            self.rec1[s[sx]] += 1
            
            if self.compare_dict(self.rec1, self.rec2):
                out += [sx - len(p) + 1]
            
        return out