class Solution {
    public int maxScore(int[] cardPoints, int k) {
        // the taks is to choose k cars
        // so get the total of all elements and check this
        // if( i - low == cardPoints.length) 
        ///         it means ==> there are k number of cards and there sum is total -sum
        int total = 0;
        for (int c: cardPoints)
            total += c;

        if (k == cardPoints.length)
            return total;

        int i = 0;
        int low = -1;
        int max = Integer.MIN_VALUE;
        int sum = 0;
        while (i < cardPoints.length) {

            sum += cardPoints[i];
            if (i - low == cardPoints.length - k) {
                max = Math.max(max, total - sum);
                sum -= cardPoints[++low];
            }
            i++;
        }

        return max;
    }
}