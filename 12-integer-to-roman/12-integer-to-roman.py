class Solution:
    def intToRoman(self, num: int) -> str:
        
        record = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        
        record = {v: k for k, v in record.items()}
        
        out = ""
        while num > 0:
            if num >= 1000:
                num = num - 1000
                out = out + f"{record[1000]}"
                continue
            if num >= 900:
                num = num - 900
                out = out + f"{record[900]}"
                continue
            if num >= 500:
                num = num - 500
                out = out + f"{record[500]}"
                continue
            if num >= 400:
                num = num - 400
                out = out + f"{record[400]}"
                continue
            if num >= 100:
                num = num - 100
                out = out + f"{record[100]}"
                continue
            if num >= 90:
                num = num - 90
                out = out + f"{record[90]}"
                continue
            if num >= 50:
                num = num - 50
                out = out + f"{record[50]}"
                continue
            if num >= 40:
                num = num - 40
                out = out + f"{record[40]}"
                continue
            if num >= 10:
                num = num - 10
                out = out + f"{record[10]}"
                continue
            if num >= 9:
                num = num - 9
                out = out + f"{record[9]}"
                continue
            if num >= 5:
                num = num - 5
                out = out + f"{record[5]}"
                continue
            if num >= 4:
                num = num - 4
                out = out + f"{record[4]}"
                continue
            if num >= 1:
                num = num - 1
                out = out + f"{record[1]}"
                continue
                
        return out