class Solution:
    def findComplement(self, num: int) -> int:
        
        # to get a gives number complement
        # 1, count number of bits
        # 2, make all bits 1 and XOR with the given number

        #1, count number of bits [both 0 and 1]
        bits = num.bit_length()

        # to make all bits 1, 2 ** bits - 1 make all bit 1
        # like 7, 15, 31, 63 ...
        all_ones = 2 ** bits - 1

        # XOR with num to flip all bits
        num ^= all_ones
        
        return num