class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    sell, prev, hold = 0, 0, -1000

    for price in prices:
      temp = sell
      sell = max(sell, hold + price)
      hold = max(hold, prev - price)
      prev = temp

    return sell