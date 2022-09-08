class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        suffix = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        
        ten_suffix = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }

        def print3digits(n):
            if n == 0:
                return ""
            
            ans = []
            if n // 100:
                ans.append(f"{suffix[n // 100]} Hundred")
                n = n % 100
            if n and n < 20:
                ans.append(f"{suffix[n]}")
            elif n and n >= 20:
                ans.append(f"{ten_suffix[n // 10]}")
                n = n % 10
                if n:
                    ans.append(f"{suffix[n]}")
            return " ".join(ans)
        
        rec = {}
        rec.update({"B": num // 1000000000})
        num = num % 1000000000
        rec.update({"M": num // 1000000})
        num = num % 1000000
        rec.update({"T": num // 1000})
        num = num % 1000
        rec.update({"Z": num})
            
        result = []
        if rec['B']:
            result.append(f"{print3digits(rec['B'])} Billion")
        if rec['M']:
            result.append(f"{print3digits(rec['M'])} Million")
        if rec['T']:
            result.append(f"{print3digits(rec['T'])} Thousand")
        if rec['Z']:
            result.append(f"{print3digits(rec['Z'])}")
        return " ".join(result)