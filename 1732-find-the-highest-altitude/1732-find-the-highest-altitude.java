class Solution {
    public int largestAltitude(int[] gain) {

        // lets user prefix sum, and store each score and compare it with the previsou max value
        int max =0;
        int sum = 0;
        int i = 0;
        while( i < gain.length){
            sum += gain[i];
            max = Math.max(max, sum);
            i++;
        }

        return max;
    }
}