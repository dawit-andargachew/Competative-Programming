class Solution {
    public int[] productExceptSelf(int[] nums) {
        // consider these cases to do these the question
        // 1, if all numbers are positive -> zeroCount == 0 then all have non-zero product
        // 2, if there is only one zero -> zeroCount == 1 
        // 3, if there are multiple zero -> zeroCount >= 2 all products becomes zero
        // we can also use the original aray without using additional space
        int zeroCount = 0;
        int products = 1;
        for(int n : nums){
            if( n == 0)// increase zeroCount if n is 0
                zeroCount++;
            else
                products *= n;
        }

        
        for(int i = 0; i < nums.length; i++){
            if(zeroCount >= 2)/// case-1
                nums[i] = 0;
            else if(nums[i] == 0 && zeroCount == 1)// case-2
                nums[i] = products;
            else if(nums[i] != 0 && zeroCount > 0)// case-2
                nums[i] = 0;
            else if(nums[i] != 0 && zeroCount == 0)// case-3
                nums[i] = products/nums[i];
        }

    return nums;        
    }
}