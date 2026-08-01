class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = len(prices)
        profit = 0
        for i in range(1, x):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit
        