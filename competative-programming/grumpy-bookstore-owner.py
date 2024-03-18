class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        n = len(customers)
        # total = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        total = 0
        for i in range( n ):
            if grumpy[i] == 0:
                total += customers[i]
        
        max_val = total
        left, right = 0, 0

        while  right < n and minutes > 0:
            if grumpy[ right ] == 1:
                total += customers[ right ]
            max_val = max( total, max_val)
            
            if right - left == minutes - 1:
                if grumpy[ left ] == 1:
                    total -= customers[ left ]
                left += 1
            right += 1

        return max_val