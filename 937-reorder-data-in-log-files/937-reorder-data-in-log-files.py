class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        res_digits = []
        res_nondigits = []

        for log in logs:
            if log.split()[1].isnumeric():
                res_digits += [log]
            else:
                res_nondigits += [log]
                
        res_nondigits.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        return res_nondigits + res_digits