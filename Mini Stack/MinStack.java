import java.util.Stack;

class MinStack {

    Stack<Integer> s;

    public MinStack() {
        s = new Stack<>();
    }

    public void push(int val) {
        s.push(val);
    }

    public void pop() {
        if (!s.empty())
            s.pop();
    }

    public int top() {
        if (s.empty())
            return -1;

        return s.peek();
    }

    public int getMin() {
        if (s.empty())
            return -1;

        int min = s.peek();
        for (Integer integer : s) {
            if (min > integer)
                min = integer;
        }

        return min;
    }

}