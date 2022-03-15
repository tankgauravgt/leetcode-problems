class Solution:
    def isHappy(self, n: int) -> bool:
        
        rec = set()
        
        while True:
            if n in rec:
                return False
            else:
                rec = rec | set([n])
                n = sum([int(c)**2 for c in str(n)])
                if n == 1:
                    return True