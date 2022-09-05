class Solution {
    public boolean isPowerOfFour(int n) {

        int remainder = 0;
        while (n < -3 || n > 3) {
            remainder = n % 4;
            if (remainder != 0)
                return false;
            n = n / 4;
        }

        return (remainder == 0 && n == 1) ? true : false;        
    }
}