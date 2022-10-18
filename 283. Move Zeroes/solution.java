class Solution {
    public void moveZeroes(int[] nums) {
           int left = 0, right = 0;

        while (right < nums.length) {
            if (nums[right] == 0)
                right++;
            else {
                int temp = nums[right];
                nums[right] = nums[left];
                nums[left] = temp;
                left++;
                right++;
            }
        }        
    }
}