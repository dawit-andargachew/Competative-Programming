// link on solutions part 
//  https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/solutions/516973/java-python-3-sliding-window-o-n-o-1-code-w-explanation-and-analysis/
class Solution {
    public int numberOfSubstrings(String s) {
        
        // the sliding windows is exluding j and including i
        int[] abc = new int[3];
        int count = 0;

        int len = s.length();

        int j = -1;// is lower pointer
        for (int i = 0; i < len; i++) {
            abc[s.charAt(i) - 'a']++;
            // You may wonder why do we need this loop, but consider this 'aaabc'
            // it has 3 substring which have 'a, b and c'
            //       so this while loop handle this scenario. when i = 3, abc =[2,1,1] and j = -1
            //          then we add until a = 0, and we come up with answer 3
            while (abc[0] > 0 && abc[1] > 0 && abc[2] > 0) {
                count += len - i;

                j++;
                abc[s.charAt(j) - 'a']--;
            }

        }

        return count;
    }
}