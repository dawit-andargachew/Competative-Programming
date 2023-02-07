class Solution {
    public int[] sortArrayByParityII(int[] nums) {

        //  lets use two points for controlling even and odd indexes
        // both even and odd numbers are equal  in size
        // step-1: for even
        //              while( even < n && nums[even] %2 ==0 )/ stops only if there is odd in the index
        //                      even += 2; 
        //step-2:for odd
        //           while( odd < n && nums[odd] %2 == 1 )/ stops only if there is even in the index
        //                      even += 2; 
        
        // step-3: interchanging these whenever these happens
        // if there is nums[odd] = even means nums[even] = odd => SO IT MUST BE INTERCHANGED

        int n = nums.length;
        int even = 0;
        int odd = 1;

        while( even < n && odd < n){
            while( even < n && nums[even] % 2 == 0)// step-1
                even += 2;
                
            while( odd < n && nums[odd] % 2 == 1)// step-2
                odd += 2;

            if( even < n && odd < n ){ // step-3
                int temp = nums[even];
                nums[even] = nums[odd];
                nums[odd] = temp;
            }

        }

        return nums;        
    }
}