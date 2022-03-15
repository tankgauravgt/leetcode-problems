class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for m in range(len(prices) - 1):
            if prices[m + 1] - prices[m] > 0:
                profit = profit + prices[m+1] - prices[m]
        return profit