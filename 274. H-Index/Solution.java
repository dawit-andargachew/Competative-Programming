
class Solution {
    static int hIndex(int[] citations) {
        
        int n = citations.length;
        int accumulate = 0;
        int[] count = new int[n + 1];// count should be [n+1] => because Math.min(n, citations)

        for (final int citation : citations)
            count[Math.min(citation, n)]++;

        // to find the largeset h-index, loop from back to front
        // i is the candidate h-index
        for (int i = n; i >= 0; i--) {
            accumulate = accumulate + count[i];
            if (accumulate >= i)
                return i;
        }

        return accumulate;
    }

}