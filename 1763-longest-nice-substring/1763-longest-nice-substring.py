class Solution:
    
    def is_nice(self, s):
        
        r = {c: 1 for c in set(s)}        
        for c in set(s):
            if r.get(c.lower(), 0) + r.get(c.upper(), 0) != 2:
                return False
        return True
    
    
    def longestNiceSubstring(self, s: str) -> str:
        
        l = 0
        r = -1
        for lx in range(len(s) - 1):
            for rx in range(len(s)):
                if self.is_nice(s[lx:rx+1]):
                    if (r - l + 1) < (rx - lx + 1):
                        l, r = lx, rx        
        return s[l:r+1]