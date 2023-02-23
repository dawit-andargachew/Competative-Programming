class Solution {
    public void rotate(int[] nums, int k) {
        if( k % nums.length == 0)
            return; 

        // lets do this in 3 steps 
        // and we need to reverse the array to it in O(1) space
        // step 1, reverse the whole array
        // step 2 reverrse the first k arrays
        // step 3 reverrse elements after k
        // if nums = 1,2,3,4,5,6,7,8,9 and k = 3
        //          9,8,7,6,5,4,3,2,1 => step 1
        //          [7,8,9],6,5,4,3,2,1 => step 2 reverse the first 3 elements
        //          7,8,9,[1,2,3,4,5,6] => step 3 reverse the rest


        // what is k > nums.length to handle this k = k%nums.length
        k = k % nums.length;

        // step 1
        int i = 0, j = nums.length - 1;
        while( i < j ){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }

        // step-2
        i = 0;
        j = k - 1; 
        while( i < j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }


        // step 3
        i = k ;
        j = nums.length - 1;
        while( i < j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }

    }
}
