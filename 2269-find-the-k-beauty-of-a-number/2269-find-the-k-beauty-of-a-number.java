class Solution {
    public int divisorSubstrings(int num, int k) {
        
        int beauty = 0;
        int low = -1;
        int i = 0;

        // Here is a slidign windows problem similar to 
        // 2379 Minimum Recolors to Get K Consecutive Black Blocks
        /// use a windows size 2 and check wether it is divisor of given number
        String s = String.valueOf(num);
        while( i < s.length()){
            if(i - low == k){
                int n = Integer.parseInt(s.substring(low + 1, i + 1));// substring(a,b), a inclusive & b exclusive
                if(n != 0 && num % n == 0)
                    beauty++;

                i++;
                low++;
            }
            else
                i++;
        }


        return beauty;        
    }
}