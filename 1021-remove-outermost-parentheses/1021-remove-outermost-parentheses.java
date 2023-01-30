class Solution {
    public String removeOuterParentheses(String s) {
        
        // lets use open to keep track of whether the parentesis is outer or not
        // if  open > 1 and '(' it is open so
        //                  append '(' and increment open
        // else if ( open > 1 ) and ')' it is open 
        //              append ')' and decrement open
        
        StringBuilder  answer = new StringBuilder();
        int open = 0;
        for(char c :s.toCharArray()){
            if(c == '('){
                if(open > 0)
                    answer.append('(');
                open++;
            }else if( c == ')'){
                if( open > 1)
                    answer.append(')');
                open --;
            }
        }
        return answer.toString();
    }
}