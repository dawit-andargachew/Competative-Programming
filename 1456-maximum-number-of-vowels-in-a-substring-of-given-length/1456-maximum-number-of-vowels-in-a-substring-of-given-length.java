class Solution {
    
    public int maxVowels(String s, int k) {
        // the question is stright forward use sliding windows and 
        // find maximum number of vowels for substring of length k

        // count the vowels and compare whether it maximum or not in each iteration
        // low is't included for the sliding windows
        char[] vowels = new char[26];
        vowels['a'-'a'] = 1;
        vowels['e'-'a'] = 1;
        vowels['i'-'a'] = 1;
        vowels['o'-'a'] = 1;
        vowels['u'-'a'] = 1;


        int max = 0;
        int low = -1;
        int i = 0;

        int count = 0;
        while( i < s.length()){
            if(vowels[s.charAt(i) - 'a'] == 1)
                count++;

            max = Math.max(max, count);            
            if(i - low == k){
                if(vowels[s.charAt(++low) - 'a'] == 1)
                    count--;
                i++;
            }
            else
                i++;
        }

        return max;        
    }
}