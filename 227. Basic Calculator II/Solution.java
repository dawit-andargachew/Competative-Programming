import java.util.Stack;

class Solution {
    public int calculate(String s) {
        int len = s.length();
        Stack<Integer> stack = new Stack<>();
        char sign = '+';
        int num = 0;
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c))
                num = num * 10 + c - '0';
            if ((!Character.isDigit(c) && c != ' ') || i == len - 1) {
                if (sign == '+')
                    stack.push(num);
                else if (sign == '-')
                    stack.push(-num);
                else if (sign == '*')
                    stack.push(num * stack.pop());
                else if (sign == '/')
                    stack.push(stack.pop() / num);
                sign = c;
                num = 0;
            }
        }
        int res = 0;
        for (Integer i : stack)
            res += i;
        return res;
    }
}
