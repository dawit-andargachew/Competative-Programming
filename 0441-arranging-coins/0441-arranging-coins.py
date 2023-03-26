class Solution:
    def arrangeCoins(self, n: int) -> int:

        l, r = 1, n
        # lets apply binary search on it
        # the minimum number of stais is 1
        while l <= r:           
            mid = ( l + r)//2
            
            total = (mid * ( mid + 1))//2
            if total == n:
                return mid
            elif total > n:
                r = mid - 1
            else:
                l = mid + 1

        return r