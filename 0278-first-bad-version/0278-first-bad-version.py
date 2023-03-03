# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low,high = 1, n
        bad = 1
        while( low <= high):
            mid = (low + high)//2
            if isBadVersion(mid):
                high = mid - 1
                bad = mid
            else:
                low = mid  + 1
        
        return bad
        """
        :type n: int
        :rtype: int
        """
        