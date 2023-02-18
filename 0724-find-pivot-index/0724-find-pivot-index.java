class Solution {
    public int pivotIndex(int[] nums) {

    //How do we check a given number is a pivot index,
    // lets store the total sum, and
    // if(total - prefixSum - nums[i] == prefixSum) => i is the prefixIndex
    //Because 
    ///         prefixSum is the sum from index i to i -1
        int total = 0;
        for(int i: nums)
            total += i;
        
        int prefixSum =0;
        int i = 0;
       while(i < nums.length){
            if(total - prefixSum - nums[i] == prefixSum)
                return i;
            // else
                prefixSum += nums[i++];
        }

        return -1;        
    }
}