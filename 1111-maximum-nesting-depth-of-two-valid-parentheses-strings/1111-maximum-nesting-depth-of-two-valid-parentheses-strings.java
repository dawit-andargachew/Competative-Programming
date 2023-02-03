class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int[] depth_array = new int[seq.length()];

// the goal is to minimize depth of a VPS by splitting all pairs of parentheses into two groups A and B. A and B can be any disjoint sub-sequence of the input sequence, as long as they are still VPS without changing the order of anything (side-note: the order constraint is implied by the word sequence).
// for more info see these links
 // - https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solutions/328920/very-easy-and-clean-code-one-pass-o-n-with-explanation/
 // - https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/solutions/358419/confused-by-this-problem-i-was-too-here-is-how-it-became-crystal-clear/
 
        int depth = 0;
        for(int i = 0; i < seq.length(); i++){
            if(seq.charAt(i) == '('){
                depth_array[i] = depth%2;
                depth ++;
            }else { //seq.chatAt(i) == ')' [It is valid]
                depth--;
                depth_array[i] = depth%2;
            }
        }


        return depth_array;
    }
}