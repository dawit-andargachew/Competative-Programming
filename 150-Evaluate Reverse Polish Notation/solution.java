import java.util.Stack;

class solution {
    public int evalRPN(String[] tokens) {
        String operators = "+-*/";

        Stack<String> stack = new Stack<>();

        for (String t : tokens) {
            if (!operators.contains(t))
                stack.push(t);
            else {
                int a = Integer.valueOf(stack.pop());
                int b = Integer.valueOf(stack.pop());

                switch (t) {
                    case "+":
                        stack.push(String.valueOf(a + b));
                        break;
                    case "-":
                        stack.push(String.valueOf(b - a));
                        break;
                    case "*":
                        stack.push(String.valueOf(a * b));
                        break;
                    case "/":
                        stack.push(String.valueOf(b / a));
                        break;
                }
            }
        }

        return Integer.valueOf(stack.pop());
    }
}