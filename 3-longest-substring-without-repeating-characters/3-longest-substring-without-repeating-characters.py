class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lx = 0
        out = 0
        rec = set([])
        for rx, c in enumerate(s):
            
            if c not in rec:            
                rec = rec | set([c])
                out = max(out, rx - lx + 1)
            else:
                while s[lx] != c:
                    rec.remove(s[lx])
                    lx = lx + 1
                lx = lx + 1
        
        return out