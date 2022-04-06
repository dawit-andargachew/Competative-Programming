import java.util.Arrays;

class Solution {
  public  int[][] kClosest(int[][] points, int k) {

        int[] Euclidean_distance = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            int x = points[i][0], y = points[i][1];
            Euclidean_distance[i] = (x * x) + (y * y);
        }

        // the Euclidean_distance is sorted
        Arrays.sort(Euclidean_distance);

        // create new array which holds Euclidean array
        int[][] eculi_array = new int[k][2];

        int max = Euclidean_distance[k - 1];
        int couter = -1;

        for (int i = 0; i < points.length; i++) {
            int x = points[i][0], y = points[i][1];

            int current_length = (x * x) + (y * y);

            if (current_length <= max && couter < k) {
                ++couter;
                eculi_array[couter][0] = x;
                eculi_array[couter][1] = y;
            }
        }

        return eculi_array;

    }

}