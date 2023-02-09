class Solution {
    public int countGoodSubstrings(String s) {
        if(s.length() < 3)
            return 0;

        int count = 0;
        for(int i =0; i < s.length() - 2; i++){
            char a = s.charAt(i);
            char b = s.charAt(i + 1);
            char c = s.charAt(i + 2);

            if(a != b && a != c && b != c)
                count++;
        }
        
        return count;
    }
}