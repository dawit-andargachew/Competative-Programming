
class Solution {
    public int[] getSumAbsoluteDifferences(int[] nums) {
        // It has formula and the formula is found in here
        // https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/solutions/969761/illustrations-for-o-n-formula-java-kotlin-python/
        int n = nums.length;
        int[] res = new int[n];
        int sumBelow = 0;
        int sumTotal = Arrays.stream(nums).sum();

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            sumTotal -= num;
            res[i] = sumTotal - (n - i - 1) * num + i * num - sumBelow;
            sumBelow += num;
        }
        return res;
    }
}