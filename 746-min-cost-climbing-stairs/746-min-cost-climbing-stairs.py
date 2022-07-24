class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def rec(n):
            nonlocal memo
            if n == 0:
                if n not in memo:
                    memo[0] = cost[0]
                return memo[0]
            elif n == 1:
                if n not in memo:
                    memo[1] = cost[1]
                return memo[1]
            else:
                if n not in memo:
                    lmin = rec(n - 1) + cost[n]
                    rmin = rec(n - 2) + cost[n]
                    memo[n] = min(lmin, rmin)
                return memo[n]
        
        rec(len(cost) - 1)
        if len(cost) > 2:
            return min(memo[len(cost) - 1], memo[len(cost) - 2])
        else:
            return min(cost)