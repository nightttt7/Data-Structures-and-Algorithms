class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m1 = prices[0]
        profit1 = 0
        m2 = 100001
        profit2 = 0
        for p in prices:
            m1 = min(m1, p)
            profit1 = max(profit1, p-m1)
            m2 = min(m2, -profit1 + p)
            profit2 = max(profit2, p-m2)
        return profit2
