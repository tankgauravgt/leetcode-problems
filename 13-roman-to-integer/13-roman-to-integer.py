class Solution:
    def romanToInt(self, s: str) -> int:
        rec = {
            'CD': 400,
            'CM': 900,
            'XL': 40,
            'XC': 90,
            'IV': 4,
            'IX': 9,
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        out = 0
        while len(s) != 0:
            if s[0:2] in rec.keys():
                out += int(rec[s[0:2]])
                s = s[2::]
                continue
            if s[0:1] in rec.keys():
                out += int(rec[s[0:1]])
                s = s[1::]
                continue
        return out