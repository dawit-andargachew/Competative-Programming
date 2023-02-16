class Solution {
    public int findMiddleIndex(int[] nums) {
        // this question is the same as 724. Find Pivot Index, 
        // The only difference is, to find the minimum among the pivot indexes
        int total = 0;
        for(int i : nums)   
            total += i;
        
        int min = Integer.MAX_VALUE;
        // to get the min privot index, initialize min with Intger.MAX_VALUE
        // if it is changed there is a pivot index, else return - 1 [no pivot index]
        int i = 0;
        int prefix = 0;

        while( i < nums.length){
            if(total - nums[i] - prefix == prefix)
                min = Math.min(min, i++);
            else
                prefix += nums[i++];
        }


        // to get the min privot index, initialize min with Intger.MAX_VALUE
        // if it is changed there is a pivot index, else return - 1 [no pivot index]
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}