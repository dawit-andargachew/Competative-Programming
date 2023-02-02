class Solution {
    public int minAddToMakeValid(String s) {
        
        /// let pop the stack if we get '(' followed by ')'
        Stack<Character> stack = new Stack();
        
        for(char c : s.toCharArray()){
            if(stack.size() > 0 && stack.peek() == '(' && c == ')')
                stack.pop();
            else 
               stack.add(c);
        }
        
        return stack.size();
    }
}