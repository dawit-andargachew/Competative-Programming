class Solution {
    public int minSwaps(String s) {
        /// for info => https://www.youtube.com/watch?v=3YDBT9ZrfaU
        // https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/solutions/1390319/how-to-reach-the-optimal-solution-explained-with-intuition-and-diagram/

        
        // to find the  minimun number of swaps we need, find the maximum number of ']' found consecutively
        // when a swap is made, it cancels two braces so the minimum swap becomes max/2
        // But, What about odd number of braces
        // to handle both odd and even number brace (max + 1)/2

        int max = 0;
        int count = 0 ;
        for(char c : s.toCharArray()){
            if( c == ']')
                count++;
            else 
                count--;
            
            max = Math.max(count,max);
        }

        return (max + 1)/2;        
    }
}