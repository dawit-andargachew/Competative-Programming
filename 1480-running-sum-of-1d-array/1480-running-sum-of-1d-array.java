class Solution {
    public int[] runningSum(int[] nums) {
        
    // lets use prefix sum with O(1) time and  O(n) space complexity
    for(int i =1; i < nums.length; i++)
            nums[i] = nums[i] + nums[i - 1];
        
    return nums;        
    }
}