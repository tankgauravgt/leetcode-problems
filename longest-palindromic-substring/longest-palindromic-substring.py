class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        cmax = ''
        for cx, c in enumerate(s):
            
            # odd palindromes:
            lx, rx = cx, cx
            while lx >= 0 and rx < len(s) and s[lx] == s[rx]:
                if len(cmax) < (rx-lx+1):
                    cmax = s[lx:rx+1]
                lx = lx - 1
                rx = rx + 1
            
            # even palindromes:
            lx, rx = cx, cx + 1
            while lx >= 0 and rx < len(s) and s[lx] == s[rx]:
                if len(cmax) < (rx-lx+1):
                    cmax = s[lx:rx+1]
                lx = lx - 1
                rx = rx + 1
                
        return cmax