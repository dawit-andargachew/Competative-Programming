class Solution {
    public int[] nextGreaterElements(int[] nums) {
        // The main question is how to make the array circular?
        //
        // Lets use an array with length, (len * 2 - 1) => [with out repeating the last element]
        // like {1,2,3,4} => {1,2,3,4,1,2,3} => have length of len*2 - 1

        // Why not len*2?
        //      becase   {1,2,3,4} => {1,2,3,4,1,2,3,4} have (len * 2 ) length
        //               {1,2,3,4} => {1,2,3,4,1,2,3} have (len * 2 - 1 ) length
        //

        // step-1: create new array and fill all the values and make it CIRCULAR ARRAY
        // step-2: fill output_array with -1, as a default
        // step-3: compare all values [nums[i] with all CIRCULAR_ARRAY values] and find the next greater element


        int len = nums.length;
        // step-1: create new array with is CIRCULAR
        int[] CIRCULAR_ARRAY = new int[2*len - 1];
        
        for(int i = 0; i < len; i++)//fill from 0 to len [including last element]
            CIRCULAR_ARRAY[i] = nums[i];

        for(int i = len; i < 2*len - 1; i++)// fill again 0 to len [excluding last element]
            CIRCULAR_ARRAY[i] = nums[i - len];// and the array becomes cirular
        

        int[] output_array = new int[nums.length];
        //step2: fill output_array with default value -1
        Arrays.fill(output_array, - 1);

        for(int i = 0; i < nums.length ; i++){
            for(int j = i + 1; j < CIRCULAR_ARRAY.length;j++){
                if(nums[i] < CIRCULAR_ARRAY[j]){// step-3
                    output_array[i] = CIRCULAR_ARRAY[j];
                    break;
                }
           }
        }
        
        return output_array;
    }
}