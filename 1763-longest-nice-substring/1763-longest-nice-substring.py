class Solution:
    
    def is_nice(self, s):
        if len(set(s)) == (2 * len(set(s.lower()))):
            return True
        return False
    
    
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) < 2:
            return ""
        
        l, r = 0, 0
        for lx in range(0, len(s), 1):
            for rx in range(lx, 1 + len(s), 1):
                if self.is_nice(s[lx:rx]):
                    if (r - l + 1) < (rx - lx + 1):
                        l, r = lx, rx
                else:
                    pass
        
        return s[l:r]