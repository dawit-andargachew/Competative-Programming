class Solution {
    public int calPoints(String[] operations) {
        
        // the question is stringht forward, just check whether the stack is empty or not for poping
        Stack<Integer> stack = new Stack();
        for(String s : operations){
            if(s.equals("C") && !stack.isEmpty()) // stack should not  empty
                stack.pop();
            else if(s.equals("D") && !stack.isEmpty()){ // stack should not be empty
                stack.push(stack.peek() * 2);
            }else if(s.equals("+") && stack.size() >= 2){// stack should be >= 2
                int second = stack.pop();
                int first = stack.peek();
                
                stack.push(second);
                stack.push(second+ first);
            }
            else// which means it is number so parse it to int
                stack.push(Integer.parseInt(s));
        }
        
        int score = 0;
        while(!stack.isEmpty())/// add all value to this
            score += stack.pop();

        return score;
    }
}