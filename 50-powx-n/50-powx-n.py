class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dNc(x, k, memo):
            
            if k < 2:
                return x ** k            
            elif k % 2 == 0:
                if k // 2 not in memo:
                    memo[k // 2] = dNc(x, k // 2, memo)
                return memo[k // 2] * memo[k // 2]
            else:
                if k // 2 not in memo:
                    memo[k // 2] = dNc(x, k // 2, memo)
                return x * memo[k // 2] * memo[k // 2]
        
        return dNc(x, n, {})