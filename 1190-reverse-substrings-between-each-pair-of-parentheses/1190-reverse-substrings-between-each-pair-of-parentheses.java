class Solution {
    public String reverseParentheses(String s) {

        // to reverse sub-string b/n each pair of parenthesis lets use stack 
        //  So, when do we reverse?
        ///         whenever we get ')', we need to reverse.
        /// step -1, push everything until we get ')'
        /// step-2, reverser the substring when we get '(', HOW? 
        //  step-3, put the letters in reverse order back to stack
        // step-4, return string

        // let s = "(abcd)",
        // step-1, push until we get ')'
        ///             then stack becomes { (, a, b, c, d}
        // step-2, we get ')'
        //             copy the stack elements unil we get '(' on to a list
        //              the list becomes {d, c, b, a} 
        // step-3, put letters in reverse order
        //       list = {d, c, b, a} => IT REVERSED
        //      so use for(int i = 0; i < list.size(); i++)
        //                   stack.push(list.get(i))
        //
        Stack<Character> stack = new Stack();
        for(char c : s.toCharArray()){
            if( c == ')'){
                List<Character> list = new ArrayList();
                while(stack.peek() != '(') // step-2
                    list.add(stack.pop());

                stack.pop();// removes ')' after putting letters on the list
                
                for(int i = 0; i < list.size(); i++)// step-3
                    stack.push(list.get(i));
                
            }else 
                stack.push(c); // step-1
        }
        
        //step-4 return string 
        StringBuilder answer = new StringBuilder();
        for(Character c : stack)
            answer.append(c);
        
        return answer.toString();
        
    }
}