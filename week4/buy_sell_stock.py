class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=prices[0]
        for i in range(len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            if maxp<prices[i]-minp:
                maxp=prices[i]-minp
        return maxp

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/