import java.util.Stack;

class MyQueue {
    private Stack<Integer> s1, s2;

    MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }

    public void push(int x) {
        while (!s1.isEmpty()) {
            s2.push(s1.pop());
        }

        s1.push(x);
        while (!s2.isEmpty()) {
            s1.push(s2.pop());
        }
    }

    public int pop() {
        if (s1.isEmpty())
            return -1;

        return s1.pop();
    }

    public int peek() {
        if (s1.empty())
            return 0;
        return s1.peek();
    }

    public boolean empty() {
        if (s1.empty())
            return true;
        return false;

    }

}
