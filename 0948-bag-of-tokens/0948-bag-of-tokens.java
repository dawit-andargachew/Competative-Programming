class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        // to maximize the score we need to store
        // sort the array and store the largest and compare it with the next scores to maximize it
        
        Arrays.sort(tokens);
        int max = 0;
        int score = 0;
        int start = 0, end = tokens.length - 1;
        while( start <= end){
            if( power >= tokens[start]){
                power = power - tokens[start];
                start++;
                score++;
                max = Math.max(score,max);
            }else if(score >= 1){
                power += tokens[end];
                end--;
                score--;
            }else 
                return max;
            
        }
        
        return max;        
    }
}