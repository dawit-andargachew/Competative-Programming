class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        
        for(char c : s.toCharArray()){
            // if( c == '(' || c == '['  || c == '{' )
            //     stack.push(c);
            if(!stack.isEmpty() && stack.peek() == '(' && c == ')')
                stack.pop();
            else if(!stack.isEmpty() && stack.peek() == '[' && c == ']')
                stack.pop();
            else if(!stack.isEmpty() && stack.peek() == '{' && c == '}')
                stack.pop();
            else
                stack.push(c);
        }
        
        if( stack.isEmpty())
            return true;
        else 
            return false;
    }
}