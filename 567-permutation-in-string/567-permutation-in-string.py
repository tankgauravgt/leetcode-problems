class Solution:
    
    def compare(self, d1, d2):
        for k in d1:
            if d1[k] != d2[k]:
                return False
        return True
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        rec1 = {c: 0 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()}
        rec2 = {c: 0 for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()}

        for c in s1:
            rec2[c] += 1
  
        for c in s2[0:len(s1)]:
            rec1[c] += 1

        if self.compare(rec1, rec2):
            return True
        
        for rx in range(len(s1), len(s2)):
            
            rec1[s2[rx - len(s1)]] -= 1
            rec1[s2[rx]] += 1
            
            if self.compare(rec1, rec2):
                return True
  
        return False