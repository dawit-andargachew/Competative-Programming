class Solution {
    public int sumOddLengthSubarrays(int[] nums) {

        // lets apply a prefix sum wiht O(n)^2 time complexity
        // we use i to determine the odd length subarrays
        // inside the second while loop we need to control whether the sub array lenth is evern or odd
        // if(top - low == i) => It is not-odd length so shift both pointers
        //
        
        int sum = 0;
        int i = 1;
        while( i <= nums.length){
            int top = 0;
            int low = 0;

            while( top < nums.length){

                if( top - low== i){  
                    low++;
                    top = low;
                }

                // before summing the sub array we need to make sure whether it is odd, it is not 
                // we need to re-arrange both pointers
                sum += nums[top];
                top++;
            }

            i = i + 2;
        }

        return sum;
    }
}