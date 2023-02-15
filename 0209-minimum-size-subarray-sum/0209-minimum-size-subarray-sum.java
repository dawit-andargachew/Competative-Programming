class Solution {
    public int minSubArrayLen(int k, int[] nums) {
        // here is a two pointer problem, just apply two pointers 

        int sum = 0;
        int min = Integer.MAX_VALUE;

        int low = -1;
        int i =0;
        while( i < nums.length){
            sum += nums[i];
            if(sum >= k){
               min = Math.min(min, i - low);
               
               while(sum >= k && low < nums.length){// reduce/shrink the sub array size unilt sum < k
                   min = Math.min(min, i - low);// take the minimum sub-array length
                   sum -= nums[++low];
               }
            }

            i++;
        }

        return min == Integer.MAX_VALUE ? 0 : min;        
    }
}