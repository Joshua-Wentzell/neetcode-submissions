class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying_price = prices[0]
        selling_price = prices[0]
        for j in range(1, len(prices)):
            i = j - 1
            if prices[i] > prices[j] and prices[j] < buying_price:
                buying_price = prices[j]
            else:
                selling_price = prices[j] - buying_price
                if selling_price > profit:
                    profit = selling_price
        return profit