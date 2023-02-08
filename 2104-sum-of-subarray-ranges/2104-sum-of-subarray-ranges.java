class Solution {
    public long subArrayRanges(int[] nums) {
        // the question is strightforward sum all the differences in the given array
        // so sorting the array is a must. and prevents from addding negative differences
        // everytime we need to check which one is min and max
        //  THIS QUESTION IS MONOTONIC STACK PROBLEM BUT IT IS A LITTLE DIFFICULT AND NEEDS SOME FORMULA
        long sum = 0;
        for (int i = 0; i < nums.length; i++) {
            int j = i;
            int min = nums[i], max = min;
            while (j < nums.length) {
                min = Math.min(min, nums[j]);
                max = Math.max(max, nums[j]);
                sum += max - min; // add differences
                j++;
            }
        }

        return sum;
    }
}