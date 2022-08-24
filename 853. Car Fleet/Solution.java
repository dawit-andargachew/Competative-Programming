import java.util.Arrays;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {

        if (position == null || position.length == 0)
            return 0;

        int n = position.length;
        // two dimenstional array to hold speed and position
        int[][] distance_speed = new int[n][2];
        for (int i = 0; i < n; i++) {
            distance_speed[i][0] = position[i];
            distance_speed[i][1] = speed[i];
        }

        // sort the 2D array based on their position
        Arrays.sort(distance_speed, (a, b) -> b[0] - a[0]);

        // store the arrival time => the time need to arrive at the destination
        float[] arrival_time = new float[n];
        for (int i = 0; i < n; i++) {
            float remainingLength = target - distance_speed[i][0];
            float Timetofinish = remainingLength / distance_speed[i][1];
            arrival_time[i] = Timetofinish;
        }

        float current = arrival_time[0];

        int carfleets = 1; // at least it has one fleet
        for (int i = 1; i < n; i++) {

            // if current car has less speed than the next one, increase the car fleet by
            // one and make current = arrival_time[i]
            if (current < arrival_time[i]) {
                carfleets++;
                current = arrival_time[i];
            }
        }

        return carfleets;

    }
}