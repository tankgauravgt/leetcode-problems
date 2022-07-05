class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        def binsearch(lx, rx):
            if rx >= lx:
                mx = lx + (rx - lx) // 2
                if (mx ** 2) < num:
                    return binsearch(mx + 1, rx)
                elif (mx ** 2) > num:
                    return binsearch(lx, mx - 1)
                else:
                    return True
            return False
        
        return binsearch(1, num)