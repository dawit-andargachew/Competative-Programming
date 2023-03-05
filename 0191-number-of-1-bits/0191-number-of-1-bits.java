public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        if (n == 0)
            return 0;
        else if (n > 0) {
            int count = 0;
            while (n > 0) {
                if (n % 2 == 1)
                    count++;
                n = n / 2;
            }
            return count;
        } else if (n < 0 & n != -2147483648) {
            int[] arr = new int[32];
            int ones = 32;
            n = Math.abs(n);

            // generate binary number in array form
            int i = 0;
            while (n > 0) {
                arr[i] = n % 2;
                n = n / 2;
                i++;
            }

            // get the first 1
            i = 0;
            while (i < 32) {
                if (arr[i] == 1) {
                    i++;
                    break;
                }
                i++;
                ones--;
            }

            // for(int bb: Solution.arr)
            // System.out.print(bb);
            // if there is another one, find it
            int other = 0;
            while (i < 32) {
                if (arr[i] == 1)
                    other++;
                i++;
            }

            return ones - other;
        } else // -2147483648
            return 1;
    }
}