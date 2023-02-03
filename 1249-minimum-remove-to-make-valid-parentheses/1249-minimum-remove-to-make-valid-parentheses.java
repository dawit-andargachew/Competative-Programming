class Solution {
    public String minRemoveToMakeValid(String s) {

        // the goal is to remove minimum number of parenthesis so that the given string becomes valid
        // let use stack, and open to track number of '(' and ')'
        //   for '(' open++
        //   for ')' open--
        // step-1: if( c == ')' && open == 0) 
        //          there no opening brace so ignore it
        //step-2: if(c == ')' and open > 0)
        //          push')' and open--
        //step-3: if( c == '(') 
        //      push'('k and open++
        //step-4: other than the above cases
        //           push to stack since their occurence doesn't matter
        //step-5: copy stack elements in to string
        //
        // step-6: What if we add '(' but there is no closing brace for them?
        //          they must be removed
        //          open controls the numbr of braces, and open > 0 means there are non-closed braces
        //          remove '(' from end of stack unti open == 0
        int open = 0;
        Stack<Character> stack = new Stack();
        
        for(char c : s.toCharArray()){
            if(c == ')' && open == 0)// step-1
                continue;
            else if(c == ')' && open > 0){// step-2
                stack.push(c);
                open--;                
            }
            else if( c == '('){// step-3
                stack.push(c);
                open++;
            }
            else// step-4: push lower case letters
                stack.push(c);
        }
        
        //step-6: remove '(' from end of stack unitl open == 0
        for(int i = stack.size() - 1; i >= 0 && open > 0;i--){
            if(stack.get(i) == '('){
                stack.remove(i);
                open--;
            }
        }

        // step-5: put stack values on to string and return it
        StringBuilder a = new StringBuilder();
        for(int i = 0; i < stack.size(); i++)
            a.append(stack.get(i));
        
        return a.toString();
    }
}