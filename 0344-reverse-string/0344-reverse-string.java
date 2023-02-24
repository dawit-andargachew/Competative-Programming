class Solution {
    public void reverseString(char[] s) {
        int start = 0;
        int end = s.length - 1;
        while( start < end){
            char c = s[start];
            s[start] = s[end];
            s[end] = c;
            end--;
            start++;
        }        
    }
}