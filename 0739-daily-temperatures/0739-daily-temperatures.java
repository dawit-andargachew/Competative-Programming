class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // similar with 
        //      1475. Final Prices With a Special Discount in a Shop
        //      496. Next Greater Element I
        // here is also a monotonic stack question, 
        // The question is simply find the next greater index, so the stack should contain the index of elements
        // Whenever the current element is greater than stack.pee() add to stack
        // else until we reach temperatuer[stack.pee()] < n 
        //          temperature[stack.peek()] = i - stack.pop();
        // 
        Stack<Integer> stack = new Stack();

        for(int i = 0; i < temperatures.length; i++){
            
            // REMBER THE STACK CONTAIN INDEX NOT values
            int n = temperatures[i];
            // n is less than temperature[stack.peek], so add to stack
            if( stack.size() == 0 || temperatures[stack.peek()] > n)
                stack.push(i);
            else{// n is greater than temperature[stack.peek()], next greate index is found
                while(stack.size() > 0 && temperatures[stack.peek()] < n)
                    temperatures[stack.peek()] = i - stack.pop();
                
                stack.push(i);
                // finally store the current index, because is becomes greater after above iteration
            }
        }

        // these elements on stack have no next greater element so make these 0
        // REMBER THE STACK CONTAIN INDEX NOT values
        while( stack.size() > 0)    
            temperatures[stack.pop()] = 0;

        return temperatures;  
    }
}