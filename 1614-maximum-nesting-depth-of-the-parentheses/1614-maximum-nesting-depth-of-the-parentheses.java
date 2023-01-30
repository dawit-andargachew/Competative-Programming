class Solution {
    public int maxDepth(String s) {
        int max = 0;
        // this question is similar with 
        // https://leetcode.com/problems/remove-outermost-parentheses/solutions/
        
        // so use open as a depth and increase it when we get '('
        // and decrease it when we get ')'
        int open = 0;        
        for(char c: s.toCharArray()){
            if(c == '(')
                open++;
            else if ( c == ')')
                open--;
            else 
                continue;
            max = Math.max(max,open);
                
        }
        
        
        return max;
    }
}