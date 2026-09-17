class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0

        for buy in range(len(prices)):
            for sell in range(buy+1, len(prices)):
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
        return maxProfit

