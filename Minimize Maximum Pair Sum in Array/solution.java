import java.util.Arrays;

class test {
    static int minPairSum(int[] nums) {

        Arrays.sort(nums);
        /*
         * to minimize max pair sum of the array  =>  { 7,2, 1,9, 3, 4,}
         * 1, sort the given array, => 1, 2,3,4,7,9
         * 2, compare the sum of => 1+9 2+7 3+7
         * meaning =>  nums[i] + nums[nums.length -(i+1)]
         */
        int maxpairsum = 0, temp = 0;
        for (int i = 0; i < nums.length / 2; i++) {
            temp = nums[i] + nums[nums.length - (i + 1)];
            if (temp > maxpairsum)
                maxpairsum = temp;
        }

        return maxpairsum;

    }

    public static void main(String[] args) {
        int[] a = { 2, 1, 3, 4 };
        System.out.println(minPairSum(a));
    }
}