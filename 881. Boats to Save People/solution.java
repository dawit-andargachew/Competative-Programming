import java.util.Arrays;

class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);

        // we need to use two pointer approach
        int start = 0;
        int end = people.length - 1;
        int min_boat = 0;

        while (start <= end) {
            if (people[start] + people[end] <= limit) {
                start++;
                end--;
                min_boat++;
            } else {
                end--;
                min_boat++;
            }

        }

        return min_boat;
    }
}