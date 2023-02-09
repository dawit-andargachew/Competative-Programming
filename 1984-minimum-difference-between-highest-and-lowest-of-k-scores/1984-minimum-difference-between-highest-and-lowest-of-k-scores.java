class Solution {
    public int minimumDifference(int[] nums, int k) {

        // the question is to minimize the difference between any k arrays
        // so sorting it makes a lot easier and use a sliding windows of size k
        Arrays.sort(nums);
        int min = Integer.MAX_VALUE;
        int i =0;
        int low = -1;

        while(i < nums.length){
            if(i - low == k){
                int difference = nums[i] - nums[low + 1];
                min = Math.min(min, difference);

                i++;
                low++;
            }
            else
                i++;
        }
        
        return min;
    }
}