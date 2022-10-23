import java.util.Arrays;
//https://www.youtube.com/watch?v=1GubKefOabc

class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {

        Arrays.sort(tokens);
        int score = 0;
        int maxscore = 0;

        int start = 0;
        int end = tokens.length - 1;

        while (start <= end) {
            if (power >= tokens[start]) {
                power -= tokens[start];
                start++;
                score++;
                maxscore = Math.max(score, maxscore);
            } else if (score > 0) { // try to get more power to maximize our score
                power += tokens[end];
                end--;
                score--;
            } else
                return maxscore;
        }

        return maxscore;
    }
}