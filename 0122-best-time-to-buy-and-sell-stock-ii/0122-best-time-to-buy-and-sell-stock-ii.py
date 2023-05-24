class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Here is a greedy problem, so what shall we do to make optimal choice at each step.
        # Lets make as much profit as we can for the current stock price we have.
        # So for each price just find one thing
        #  - its nearest largest value in the given increasing subarray to get max profit,
        #     example-1 take [7,1,5,3,6,4]
        #          increasing subarrays are [1,5] [3,6]
        #               then profit becomes 5-1, 6-3 => profit 7

        #      example-2 take [7,1,3,5,6,4]
        #           increasing subarray is only [1,3,5]
        #               then profit beomes 5-1 => profit is 4

        small, profit, i = prices[0], 0, 0

        while i < len(prices):

            # take the first smallest value we have
            while i < len(prices) -1 and prices[i] > prices[i + 1]:
                i += 1
            
            # we reached the last index, break the loop
            if i >= len(prices) - 1:
                break
            
            # take the smallest value
            small = prices[i]

            # find the largest value we can have
            while i < len(prices) -1 and prices[i] < prices[i + 1]:
                i += 1
                
            # the profit we can made for out optimal choice
            profit += prices[i] - small
            
            # the index is in range, so the next value become minimum element
            if i < len(prices):
                small = prices[i]

            i += 1

        return profit