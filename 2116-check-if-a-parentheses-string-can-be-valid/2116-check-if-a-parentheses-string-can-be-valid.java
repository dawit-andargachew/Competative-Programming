class Solution {
    public boolean canBeValid(String s, String locked) {
        // similar to this question => 678. Valid Parenthesis String
        // but in here unlocked parenthesis can be open or closed 
        // And we need to keep the index of locked and unlocked parenthesis
        // so let use two stacks one p_locked => keep locked parenthesis and unlocked => for unlocked parenthesis
        //  step-1: if(locked[i] == 0)
        //           unlocked.push(i)
        // step-2: if(locked[i] == 1 && s.charAt(i)== '(')
        //          p_locked.push(i)      
        // step-3: if( locked[i] == 1 && s.charAt(i) == ')')
        //                case-1: if p_locked.size() > 0 => p_locked.pop()
        //                case-2: else if unlocked.size() > 0 => unlocked.pop() 
        //                case-3: else [both unlocked and p_locked are empty so IT is invalid]
        //                          like this ")()()", [1,0,0,0,0] 
        //                          the first parenthesis is locked, it does't have closing brace. So it's invalid
        // 
        // Step-4: But what if "((()()" [1,1,0,0,0] 
        //           "((" are locked
        //            "()()" are unlocked ?????????
        // Hence, until p_locked.peek() < unlocke.peek()
        //              pop both of them

        // Step-5: then finally to be valid two things must be fulfiled
        //    1, p_locked must be empty
        //    2, unlocked must have evern length so that each can be cancelled out 
        // 

        Stack<Integer> unlocked = new Stack();
        Stack<Integer> p_locked = new Stack();

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);

            if(locked.charAt(i) == '0')// step-1
                unlocked.push(i);
            else if(locked.charAt(i) == '1' && c == '(')// step-2
                p_locked.push(i);
            else if(locked.charAt(i) == '1' && c == ')'){// step-3
                if(p_locked.size() > 0)// case -1
                    p_locked.pop();
                else if( unlocked.size() > 0)// case-2
                    unlocked.pop();
                else/// case-3
                    return false;
            }
        }
        
         // step-4, make sure if locked parenthesis cab be cancled by unlocked
        while( p_locked.size() > 0 && unlocked.size() > 0 && unlocked.peek() > p_locked.peek()){
            p_locked.pop();
            unlocked.pop();
        }

        // step-5: check it is valid or not
        if(p_locked.size() == 0 && unlocked.size()%2 == 0)
            return true;
        else 
            return false;        
    }
}