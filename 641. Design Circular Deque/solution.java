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