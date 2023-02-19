class Solution {
    public int[] nextGreaterElements(int[] nums) {
        
        int len = nums.length;
        // lets copy the array twice and make it circular
        int[] circ = new int[2 * len];
        int i = 0;
        for(int n : nums)
            circ[i++] = n;

        for(int n : nums)
            circ[i++] = n;

        int[] next = new int[len];
        Arrays.fill(next, - 1);

        Stack<Integer> stack = new Stack();
        for(int j = 0; j < circ.length; j++){
            
            while(stack.size() > 0 && circ[stack.peek()] < circ[j])
                next[stack.pop() % len] = circ[j];// stack contais indexes of circ, 
                                                  // so stack.pop() % len, make the index suitable for array next

            stack.push(j);
        } 

        return next; 
    }
}