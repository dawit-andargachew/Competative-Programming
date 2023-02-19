class Solution {
  public void moveZeroes(int[] nums) {

    int index = 0;
    for (int j = 0; j < nums.length; j++)
      if (nums[j] != 0) 
        nums[index++] = nums[j];

    for (int i = index; i < nums.length; i++)
      nums[i] = 0;
  }
}