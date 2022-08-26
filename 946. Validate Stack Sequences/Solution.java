import java.util.Stack;

class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {

        Stack<Integer> st = new Stack<>();
        int pointer = 0;

        for (int n : pushed) {
            st.push(n);

            while (!st.isEmpty() && st.peek() == popped[pointer]) {
                st.pop();
                pointer++;
            }
        }
        return st.isEmpty();

    }
}