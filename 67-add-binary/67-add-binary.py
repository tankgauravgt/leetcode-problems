class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        c = 0
        out = ''
        while len(a) > 0 and len(b) > 0:
            _sum = c + int(a[-1]) + int(b[-1])
            out = str(_sum % 2) + out
            c = _sum // 2
            a = a[0:-1:1]
            b = b[0:-1:1]
        
        while len(a) > 0:
            _sum = c + int(a[-1])
            out = str(_sum % 2) + out
            c = _sum // 2
            a = a[0:-1:1]

        while len(b) > 0:
            _sum = c + int(b[-1])
            out = str(_sum % 2) + out
            c = _sum // 2
            b = b[0:-1:1]
        
        if c == 1:
            out = '1' + out
        
        return out