class Solution {
    public int maxSumTwoNoOverlap(int[] nums, int firstLen, int secondLen) {
        // The goal is to find non-overlapping subarrays, the question is simply
        // 1,find non-overlapping sub-array sums of length firstLen and secondLen
        //      for this use two while loops
        //         one to find secondLen sub-arrays after firstLen
        //         two to find secondLen sub-arrays before firstLen
        // 2, track sub-array sums
        //      for this put the prefixsum in each nums[i]
        //      because finding the sub-array sum becomes simple if nums[i] holds the prefix sum

        // change every array element with its prefix sum
        // handles qeustion-1
        for(int i =1; i < nums.length; i++) 
            nums[i] = nums[i] + nums[i-1];

        int max = 0;// holds the max sum 

        int i = 0;
        int low = -1;
        while( i < nums.length){ // handles question - 1

            // sub-array size is firstLen, so lets find left and right sub-array of length secondLen if there exist
            if(i - low == firstLen){

                int j = i ;
                int low_j = i+1;
                // helps to find secondLen sub-arrays found after firstLen
                while( j < nums.length){ 

                    if(j - low_j == secondLen){
                        int sum = (low == -1)? nums[i] : nums[i] - nums[low];
                        sum += nums[j] - nums[low_j++];
                        max = Math.max(max, sum);
                    }
                    j++;
                }


                int k = 0;
                int low_k = -1;
                // helps to find secondLen sub-arrays found before firstLen
                while( low + 1 >= secondLen && k < low + 1){

                    if(k - low_k == secondLen){
                        int sum = (low == -1)? nums[i] : nums[i] - nums[low];
                        sum += (low_k == -1)? nums[k] : nums[k] - nums[low_k];
                        max = Math.max(max, sum);
                        low_k++;
                    }
                    k++;
                }


                low++;// increase the sliding window buttom pointer 
            }
            

            i++;
        }


        return max;
    }
}