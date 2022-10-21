class Solution {
    public void rotate(int[] nums, int k) {

        // if k > nums.lenth, k should be the remainder
        if (k > nums.length)
            k = k % nums.length;

        int[] temp = new int[k]; // temp array to store rotated array elements

        int index = 0;
        int len = nums.length;

        // store in temp array
        for (int i = Math.abs(len - k); i < len; i++) {
            temp[index] = nums[i];
            index++;
        }

        // move the arrays k directions forward
        for (int i = len - k - 1; i >= 0; i--)
            nums[i + k] = nums[i];

        // put the array back
        for (int i = 0; i < k; i++)
            nums[i] = temp[i];
    }
}