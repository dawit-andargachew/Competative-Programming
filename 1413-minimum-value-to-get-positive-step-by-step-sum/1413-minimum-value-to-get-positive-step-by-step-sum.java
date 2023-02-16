// class Solution {
//     public int minStartValue(int[] nums) {
        
//         // the goal is to find the minvalue where when we sum up all values of nums it is always >= 1
//         // so why don't we find the minimum sum and
//         // if minPrefixsum >= 1, minimum start value becomes 1 
//         // else if minPrefixsum is negative 
//         //      multiply with -1 , then the sum is 0. But the goal is >= 1
//         ///     so add 1, Now it is 1
//         // NOTE: for 0 => 0 * -1 + 1 is alow works
        
//         int minPrefixsum = nums[0];
//         int tempsum = nums[0];
//         for(int i = 1; i < nums.length; i++){
//             tempsum += nums[i];
//             if( minPrefixsum > tempsum)
//                 minPrefixsum = tempsum;
//         }
        
//         if(minPrefixsum >= 1)/// if minPrefixsum is >=1 min value is 1 by default
//             return 1;
//         else // else convert it to positive number and add 1 to it
//             return (minPrefixsum * -1) + 1;
//     }
// }

// SAME BUT BETTER IMPLEMENTATION

class Solution {
    public int minStartValue(int[] nums) {
        int i = 0;
        int sum = 0;
        int min = Integer.MAX_VALUE;

        while(i < nums.length){
            sum += nums[i++];
            min = Math.min(min, sum);
        }

    
        return min < 0? -1 * min + 1: 1;// if min > 0, return 1 else -1*min + 1 to make sure all sum is > 1
    }
}