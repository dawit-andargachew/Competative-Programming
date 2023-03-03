class Solution(object):
    def mySqrt(self, x):
        low, high = 1, x
        ans = 0
        
        while low <= high:
            mid =( low + high)//2
            
            if mid**2 > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        
        return ans
        """
        :type x: int
        :rtype: int
        """
        