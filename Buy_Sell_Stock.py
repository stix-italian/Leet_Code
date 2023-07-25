# got it first run and first submit!

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = prices[0]
        sell = -1
        amount = 0
        for x in range(1,len(prices)):
            if prices[x] < buy:
                buy = prices[x]
                sell = prices[x]
            else:
                if prices[x] > sell:
                    sell = prices[x]
                    if amount < (sell - buy):
                        amount = sell - buy
            
        return amount