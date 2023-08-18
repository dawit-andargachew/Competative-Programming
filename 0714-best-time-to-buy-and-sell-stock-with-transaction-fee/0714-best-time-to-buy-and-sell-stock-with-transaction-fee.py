class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo=[0,0]
        for i in range(1,len(prices)):
            grow=prices[i]-prices[i-1]
            memo[0],memo[1]=max(memo[0],memo[1]+grow-fee),max(memo[0],memo[1]+grow)

        return memo[0]