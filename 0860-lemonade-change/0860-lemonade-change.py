class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:

            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            elif bill == 20:
                if ten == 0:
                    five -= 2
                else:
                    ten -= 1
                five -= 1

            # if there is a negative bill, we can't provide correct change
            if five < 0 or ten < 0:
                return False

        return True