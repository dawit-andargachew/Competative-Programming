class Solution {
    public int longestOnes(int[] nums, int k) {
        // is a sliding window prolem similar to 2379. Minimum Recolors to Get K Consecutive Black Blocks
        int max = Integer.MIN_VALUE;
        int zeros = 0;

        int j = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0)
                zeros++;
            
            if(zeros > k){
                // skps if there are only ones 1 1 0 0 1 1 1 0 1 1, k = 2
                //                   j = index 0           i = index 7 => j shold point to the second zero
                //                   so iterate to pass these two 1
                // and j stops when it hits zero, so increase to 
                while(nums[j] != 0)
                    j++;
                
                j++;// remove one zeros
                zeros--;// decrease zero by one
            }

            max = Math.max(max, i - j + 1);
        }

        return max;
    }
}