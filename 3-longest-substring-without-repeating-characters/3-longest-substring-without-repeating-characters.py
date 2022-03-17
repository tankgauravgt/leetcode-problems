class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lx = 0
        rec = set([])
        
        cmax = 0
        for rx, c in enumerate(s):
            if c not in rec:
                rec = rec | set([c])
                cmax = max(cmax, rx - lx + 1)
            else:
                while s[lx] != c:
                    rec.remove(s[lx])
                    lx = lx + 1
                lx = lx + 1
        
        return cmax