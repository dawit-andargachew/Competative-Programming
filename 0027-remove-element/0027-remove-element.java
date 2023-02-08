class Solution {
    public int removeElement(int[] nums, int val) {

        // the goal is to put the non-val numbers in the first k slot of nums
        // use index to keep the index and everytime check this
        //      if( i != val)
        //          nums[index++] = i;

        //  index is also the number of elements in the aray which are non-val

        int index = 0;
        for(int i : nums){
            if(i  != val){// if is different from val, put in the array
                nums[index] = i;
                index++;
            }
        }


        return index;        
    }
}