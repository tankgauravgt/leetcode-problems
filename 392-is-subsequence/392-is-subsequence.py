class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        lx = 0
        rx = 0
        while lx < len(s) and rx < len(t):
            if s[lx] == t[rx]:
                lx = lx + 1
                rx = rx + 1
            else:
                rx = rx + 1
        
        if lx < len(s):
            return False
        else:
            return True