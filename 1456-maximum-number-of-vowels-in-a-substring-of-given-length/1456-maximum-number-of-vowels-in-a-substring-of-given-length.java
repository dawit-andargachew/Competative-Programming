class Solution {
    
    public int maxVowels(String s, int k) {
        // the question is stright forward use sliding windows and 
        // find maximum number of vowels for substring of length k

        // count the vowels and compare whether it maximum or not in each iteration
        // low is't included for the sliding windows
        List<Character> vowels = new ArrayList();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');


        int max = 0;
        int low = -1;
        int i = 0;

        int count = 0;
        while( i < s.length()){
            if(vowels.contains(s.charAt(i)))
                count++;

            max = Math.max(max, count);            
            if(i - low == k){
                if(vowels.contains(s.charAt(++low)))
                    count--;
                i++;
            }
            else
                i++;

        }

        return max;        
    }
}