from itertools import combinations

class Solution:
    
    def compare(self, c, o):
        for k in o.keys():
            if o[k] != c.get(k, None):
                return False
        return True
    
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        rec = {}
        for word in words:
            if word not in rec:
                rec[word] = 1
            else:
                rec[word] += 1
        
        out = []
        for lx in range(len(s) - (len(words) * len(words[0])) + 1):
            
            tmp = {}
            for ix in range(len(words)):
                temp_str = s[lx+ix*len(words[0]):lx+(ix+1)*len(words[0])]
                if temp_str not in tmp:
                    tmp[temp_str] = 1
                else:
                    tmp[temp_str] += 1
            
            if self.compare(tmp, rec):
                out += [lx]
            
        return out