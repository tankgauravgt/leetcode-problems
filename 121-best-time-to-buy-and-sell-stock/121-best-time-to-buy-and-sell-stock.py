class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cmin = float('inf')
        for ix in range(len(prices)):
            if prices[ix] < cmin:
                cmin = prices[ix]
            elif max_profit < prices[ix] - cmin:
                max_profit = prices[ix] - cmin
        return max_profit