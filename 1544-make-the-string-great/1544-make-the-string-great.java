class Solution {
  public String makeGood(String s) {

      // this question is similar to https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
      // and the difference between 'E' and 'e' is -32, becomes 32 when interchanged
      // so use Math.abs() and compare it with 32
    Stack < Character > stack = new Stack();

    for (char c: s.toCharArray()) {

      if (!stack.isEmpty() && Math.abs(stack.peek() - c) == 32)
        stack.pop();
      else
        stack.add(c);
    }

    StringBuilder a = new StringBuilder();
    for (Character c: stack)
      a.append(c);
    return a.toString();
  }
}