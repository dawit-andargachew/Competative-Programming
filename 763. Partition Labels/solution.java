import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> partitionLabels(String s) {

        // store the last occurrence of each letters so that we can
        // maximize partition size
        int[] lastIndexes = new int[26];
        for (int i = 0; i < s.length(); i++)
            lastIndexes[s.charAt(i) - 'a'] = i;

        List<Integer> part = new ArrayList<>();
        int prev = -1;
        int max = 0;

        for (int i = 0; i < s.length(); i++) {
            max = Math.max(max, lastIndexes[s.charAt(i) - 'a']);

            // if i = last occurrene of a give letter partition it
            if (max == i) {
                part.add(max - prev);
                prev = max;
            }
        }

        return part;
    }
}