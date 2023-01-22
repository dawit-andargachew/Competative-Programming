class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        // to get the maximum number of subsequence sort nums
        // then check whether the subsequence sum is greater or not of queries[i]
        // and keep track of the subsequence size
        // it is greater store in the answer array
        
        
        int[] answer = new int[queries.length];
        
        Arrays.sort(nums);// sort nums
        for(int i = 0; i < queries.length; i++){
            int sum = 0;
            int subsequence = 0; // keep track of subsequence size for each queries
            for(int n : nums){
                sum += n;
                if( sum > queries[i])
                    break;
                subsequence++;
            }
            
            answer[i] = subsequence;// store the subsequence size
        }
        
        return answer;
    }
}