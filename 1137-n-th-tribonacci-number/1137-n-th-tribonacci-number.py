class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n < 3:
            return int(n > 0)
        
        T0, T1, T2 = 0, 1, 1
        for k in range(n - 2):
            T2, T1, T0 = T0 + T1 + T2, T2, T1
        return T2