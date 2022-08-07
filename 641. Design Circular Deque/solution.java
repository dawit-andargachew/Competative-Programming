import java.util.Stack;

class MyCircularDeque {
    Stack<Integer> deque = new Stack<>();
    int size;

    public MyCircularDeque(int k) {
        size = k;
    }

    public boolean insertFront(int value) {
        if (isFull())
            return false;
        deque.add(0, value);
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull())
            return false;

        deque.push(value);
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty())
            return false;

        deque.remove(0);
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty())
            return false;

        deque.pop();
        return true;
    }

    public int getFront() {
        if (isEmpty())
            return -1;

        return deque.get(0);
    }

    public int getRear() {
        if (isEmpty())
            return -1;

        return deque.peek();
    }

    public boolean isEmpty() {
        if (deque.isEmpty())
            return true;

        return false;
    }

    public boolean isFull() {
        if (deque.size() == size)
            return true;

        return false;
    }
}


/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */