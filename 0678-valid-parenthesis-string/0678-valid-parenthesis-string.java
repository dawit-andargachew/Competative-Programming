class Solution {
    public boolean checkValidString(String s) {
        // lets use two stack, one for '(' and ')', another for keeping '*'

        // since '*' can be used as '(' or ')' or "" we need track is location
        //         "***(" => invalid
        //         "(***" => valid
        //         ")***(" => invalid
        //         "***" => valid, etc...

        // so we need to use two stacks, closed_p => track closed parenthesis and star => track '*' locations
        // step-1: whenever we get '(', push its location
        // step-2: when we get ')', consider the following cases
        //      case-1: if(close_p.size() == 0 && star.size() == 0)
        //                 return false. B/ce ")" comes first. It is invalid like ")***", ")()()"
        //      case-2: if(close_p.size() > 0) 
        //              there is closed parenthesis so pop it
        //      case-3: if(star.peek() < i) 
        //              it is like ***), consider '*' as closing brace and pop it
        //step-3: What if, strings like "(***" exis?, They are valid and we need use '*' closing brace

        // so until closed_p.pee() < star.peek(), pop both of them
        // Finally, if closed_p.size() == 0 => is Valid if not it is inValid


        Stack<Integer> closed_p = new Stack();
        Stack<Integer> star = new Stack();

        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '(')/// step-1: when we get '(', push its location
                closed_p.push(i);
            else if( s.charAt(i) == ')'){
                if(closed_p.size() == 0 && star.size() == 0)// case-1
                    return false;
                else if( closed_p.size() > 0 )// case-2
                        closed_p.pop();
                else if( star.peek() < i)// case-3
                    star.pop();
                // else=> consider if(closed_p().size() ==0 && star.size() ==0) as else condition
                //     return false;
            }            
            else if( s.charAt(i) == '*')//when we get '*', store its location
                star.push(i);
        }

        //step-3, if there are opening braces, consider star as closing brace based on this condition
       while(star.size() > 0 && closed_p.size() > 0 && star.peek() > closed_p.peek()){
            star.pop();
            closed_p.pop();
        }

        return closed_p.isEmpty();        
    }
}