class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        profit = 0
        for p in prices:
            if p >= m:
                if p - m > profit:
                    profit = p - m
            else:
                m = p
        return profit
