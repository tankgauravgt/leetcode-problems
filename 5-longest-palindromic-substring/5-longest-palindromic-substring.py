class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        cmax = ""
        for cx, c in enumerate(s):
            
            temp = ""
            
            # check for even:
            lx = cx
            rx = cx + 1
            while rx < len(s) and lx >= 0:
                # print('EVEN', lx, rx)
                if s[rx] == s[lx]:
                    temp = s[lx] + temp + s[rx]
                    rx = rx + 1
                    lx = lx - 1
                else:
                    break

            if len(temp) > len(cmax):
                cmax = temp
                    
            temp = ""
            
            # check for odd:
            lx = cx
            rx = cx
            while rx < len(s) and lx >= 0:
                # print('ODD', lx, rx)
                if s[lx] == s[rx]:
                    if temp == "":
                        temp = s[lx]
                    else:
                        temp = s[lx] + temp + s[rx]
                    rx = rx + 1
                    lx = lx - 1
                else:
                    break
            
            if len(temp) > len(cmax):
                cmax = temp
        
        return cmax