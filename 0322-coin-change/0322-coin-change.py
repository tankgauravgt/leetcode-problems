class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(rem, coins, memo):
            if rem < 0:
                return float('inf')
            elif rem == 0:
                return 0
            elif rem in memo:
                return memo[rem]
            else:
                min_val = float('inf')
                for coin in coins:
                    min_val = min(min_val, 1 + dp(rem - coin, coins, memo))
                memo[rem] = min_val
                return min_val
        
        res = dp(amount, coins, {})
        if res != float('inf'):
            return res
        return -1