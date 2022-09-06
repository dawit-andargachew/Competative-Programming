import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<String> str = new Stack<>();
        Stack<Integer> num = new Stack<>();
        String result = "",temp = "";
        int count = 0, k = 0;;

        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i)))
                count = count * 10 + s.charAt(i) - '0';
            else if (s.charAt(i) == '[') {
                num.push(count);
                str.push(result);
                count = 0;
                result = "";
            } else if (s.charAt(i) == ']') {
                 k = num.pop();
                 temp = str.pop();
                while (k > 0) {
                    temp = temp + result;
                    k--;
                }
                result = temp;
            } else {
                result = result + s.charAt(i);
            }
        }

        return result;
        
    }
}