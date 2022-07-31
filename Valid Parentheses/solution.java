import java.util.Stack;

class Solution {
    public boolean isValid(String s) {

        if (s.length() % 2 != 0)
            return false;

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {

            switch (c) {
                case '(':
                case '[':
                case '{':
                    stack.push(c);
                    break;
                case ')':
                    if (stack.empty() || stack.peek() != '(')
                        return false;
                    else
                        stack.pop();
                    break;
                case ']':
                    if (stack.empty() || stack.peek() != '[')
                        return false;
                    else
                        stack.pop();
                    break;
                case '}':
                    if (stack.empty() || stack.peek() != '{')
                        return false;
                    else
                        stack.pop();
                    break;
            }
        }

        return stack.isEmpty();
    }
}