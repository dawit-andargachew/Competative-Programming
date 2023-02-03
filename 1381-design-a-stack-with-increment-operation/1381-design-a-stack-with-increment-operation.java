class CustomStack {
    
    int maxSize;
    Stack<Integer> stack;

    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        stack = new Stack();
    }
    
    public void push(int x) {
        if(stack.size() < maxSize)
            stack.push(x);
    }
    
    public int pop() {
        if(stack.size()  == 0)
            return -1;
        else 
            return stack.pop();
    }
    
    public void increment(int k, int val) {
        // What if the k > stack.size()???
        // stack.size() < k, means k must equal with stack.size() else error
        k = Math.min(k, stack.size());
        for(int i = 0; i < k; i++)
            stack.set(i, stack.get(i) + val);// increment each value with val amount
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */