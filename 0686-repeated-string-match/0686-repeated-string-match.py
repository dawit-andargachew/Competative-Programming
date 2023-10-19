class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n1 = len(a)
        n2 = len(b)

        def fun(value, a, b):
            new_string = a * value
            if b in new_string:
                return True
            else:
                return False

        low = 1
        high = math.ceil(n2 / n1) + 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if fun(mid, a, b):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
