class Solution {
    public int minAddToMakeValid(String s) {
        
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