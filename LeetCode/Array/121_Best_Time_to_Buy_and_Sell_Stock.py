"""
121. Best Time to Buy and Sell Stock - Easy
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0. 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import ContextManager


prices = [7,6,4,3,1]
max_profit  = 0
current_profit  = 0

"""for i in range(len(prices)):
    j = i+1
    for j in range(len(prices)):
        print(prices[i],prices[j])

        if prices[i] < prices[j]:
            current_profit = prices[j] - i
            #print(f"current : {current_profit}")
        elif prices[i] > prices[j]:
            j +=1
        elif current_profit > max_profit :
            max_profit = current_profit"""


def maxProfit(prices):
        max_profit = 0
        minimum_num = 100000

        for num in prices:
            if num < minimum_num:
                minimum_num = num
            max_profit = max(max_profit, num - minimum_num)
        return max_profit


print(max_profit(prices)) 

