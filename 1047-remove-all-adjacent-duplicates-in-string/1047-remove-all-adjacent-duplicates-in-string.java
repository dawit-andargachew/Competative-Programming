class Solution {
    public String removeDuplicates(String s) {
        
    /// we can use stack and if the top element is equal to current 
    // and we can keep track of weather they are duplicate or not
    Stack<Character> stack = new Stack();
      for(char c : s.toCharArray()){
        if(stack.size() > 0 && stack.peek() == c)
            stack.pop();
         else
            stack.add(c);
        }

        // char[] a = new char[stack.size()];
        StringBuilder a = new StringBuilder();
        for(int i = 0; i < stack.size(); i++)
            a.append(stack.get(i));

        return String.valueOf(a);
    }
}
