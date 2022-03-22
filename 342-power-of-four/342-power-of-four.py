class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4:
            return n == 1
        
        while n >= 4:
            if n % 4 != 0:
                return False
            n = n // 4
        return n == 1