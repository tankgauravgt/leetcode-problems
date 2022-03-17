class Solution:
    def myAtoi(self, s: str) -> int:
        
        res = 0
        s = str(s).lstrip(' ')
        
        if len(s) > 1 and s[0] == '-':
            for ix, n in enumerate(s[1::]):
                if n in '0123456789':
                    res = ((res * 10) - int(n))
                else:
                    break
        
        elif len(s) > 1 and s[0] == '+':
            for ix, n in enumerate(s[1::]):
                if n in '0123456789':
                    res = ((res * 10) + int(n))
                else:
                    break
        
        else:
            for ix, n in enumerate(s):
                if n in '0123456789':
                    res = ((res * 10) + int(n))
                else:
                    break
        
        if res < -(2**31):
            res = -(2**31)
        if res > +(2**31 - 1):
            res = (2**31) - 1
            
        return res