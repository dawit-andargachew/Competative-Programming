class Solution {
    public int longestSubarray(int[] nums) {
        // here is the same as 1004. Max Consecutive Ones III
        // just in this case considet we can only flip one zero
        int max = Integer.MIN_VALUE;
        int zero = 0;
        int low = 0;

        int i = 0;
        while( i < nums.length){
            if(nums[i] == 0)
                zero++;
            if(zero > 1){
                while( nums[low] != 0)
                    low++;

                low++;// jumps the last occurence of zero
                zero--;// decrease zeros by one
            }

            max = Math.max(max, i - low);
            i++;
        }

        return max;        
    }
}