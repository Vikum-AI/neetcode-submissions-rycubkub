class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        p1, p2 = 0, 1
        max_profit = 0

        while p2 < len(prices):
            if prices[p2] < prices[p1]:
                p1 = p2
                p2 += 1
                continue

            profit = prices[p2] - prices[p1]
            max_profit = max(max_profit, profit)

            p2 += 1

        return max_profit