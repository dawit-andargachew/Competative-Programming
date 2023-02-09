class Solution {
    public int minimumRecolors(String blocks, int k) {

        // the size of sliding window is 7, b/n low and i [excluding low ]
        // everytime the window size is 7, update the lowest and check weather the lowes is 'w' or not
        int min = Integer.MAX_VALUE;
        int low = -1;
        int white = 0;

        for (int i = 0; i < blocks.length(); i++) {
            if (blocks.charAt(i) == 'W')
                white++;

            if (i - low == k) { // the window reaches size of k.
                min = Math.min(min, white); // update  minimum.

                // slide 1 step right the lower bound of the sliding
                // window and update the value of white count.
                low++;
                if (blocks.charAt(low) == 'W')
                    white--;
            }
        }


        return min;
    }
}