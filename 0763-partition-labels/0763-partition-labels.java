
class Solution {
    public List<Integer> partitionLabels(String s) {

        // store the last occurrence of each letters so that we can
        // maximize partition size to do this we need int array with size of 26 
        // step 1, store the last occurence of each character
        // step 2, if [ current character_index == last_occurence [charact - 'a']] => we need partitioning
        ///         so how do we control each partition size, [we need to store is previos partition size]
        // But the array is zero based so, previos = - 1 initially

        // step - 1, store the last occurence of each character
        int[] last_occurence = new int[26];
        for (int i = 0; i < s.length(); i++)
            last_occurence[s.charAt(i) - 'a'] = i;

        List<Integer> part = new ArrayList<>();
        int prev = -1;// should be -1, because the array is zero based
        int max = 0;

        // step - 2
        for (int i = 0; i < s.length(); i++) {
            max = Math.max(max, last_occurence[s.charAt(i) - 'a']);

            // if i = last occurrene of a give letter partition it
            if (max == i) {
                part.add(max - prev);
                prev = max;// store is previos partition size, all partition size should be equal to original size
            }
        }

        return part;
    }
}