from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        lx = 0
        rx = 0
        cmax = 0
        rec = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'.upper()}
        
        cost = 0
        while rx >= lx and rx < len(s):
            if cost <= k:
                rec[s[rx]] += 1
                rx = rx + 1
                cost = (rx - lx) - max(rec.values())
            else:
                rec[s[lx]] -= 1
                lx = lx + 1
                cost = (rx - lx) - max(rec.values())
            
            # print(s[lx:rx], cost)
            
            if cost <= k:
                cmax = max(cmax, rx - lx)
        
        return cmax