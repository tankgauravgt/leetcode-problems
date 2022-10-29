class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(coins, csum, target, memo):
            if csum == target:
                return 0
            elif csum > target:
                return float('inf')
            elif csum in memo:
                return memo[csum]

            min_val = float('inf')
            for coin in coins:
                if csum + coin <= target:
                    min_val = min(min_val, 1 + dfs(coins, csum + coin, target, memo))
            memo[csum] = min_val
            return memo[csum]

        res = dfs(coins, 0, amount, {})
        return res if res != float('inf') else -1