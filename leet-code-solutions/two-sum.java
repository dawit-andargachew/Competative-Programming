class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = { 0, 0 };
        for (int i = 0; i <= nums.length - 2; i++) // i = 0 ; i < size -1 ; i ++
        {
            for (int j = i + 1; j <= nums.length - 1; j++) // j = i + 1; j < size ; j ++
            {
                if (nums[i] + nums[j] == target && i !=j) {
                    answer[0] = i;
                    answer[1] = j;
                    break;
                    
                }
            }
        }
        return answer;
        
    }
}