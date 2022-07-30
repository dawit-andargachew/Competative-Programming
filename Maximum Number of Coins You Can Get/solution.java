import java.util.Arrays;

class solution {
    static int maxCoins(int[] piles) {

        Arrays.sort(piles);
        /*
         * the max coin problem works like this
         * give array => 2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30
         * after sort => 1,2,3,4,5,6,7,8,9,10,20,30
         * then add -> 5,7,9 and 20 starting from len -2, by decreasing i by 2
         * until ++j == len/3
         */
        int j = 0;
        int len = piles.length;
        int coins_sum = 0;
        for (int i = len - 2;; i -= 2) {
            coins_sum += piles[i];
            if (++j == len / 3) {
                return coins_sum;
            }
        }

        // return coins;

        /*
         * this return statement becomes unreachable because the for loop
         * is infinite => without exit condition
         * 
         * to use the above return statement => add exit condition in the for loop
         * for(int i =len -2; i>0; i-= 2)
         */

    }

    public static void main(String[] args) {
        int[] a = { 2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30 };
        System.out.println(maxCoins(a));
    }
}