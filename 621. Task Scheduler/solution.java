class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] letters = new int[26];

        for (char ch : tasks)
            letters[ch - 'A']++;

        int max = Integer.MIN_VALUE;

        for (int count : letters)
            max = Math.max(max, count);

        max--;

        int spaces = max * n + max;

        for (int count : letters)
            spaces -= Math.min(count, max);

        return spaces > 0 ? tasks.length + spaces : tasks.length;
    }
}