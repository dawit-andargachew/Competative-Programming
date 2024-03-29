import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int rows = matrix.length;
        int columns = matrix[0].length;
        int up = 0;
        int left = 0;
        int right = columns - 1;
        int down = rows - 1;

        while (result.size() < rows * columns) {
            // Left to right direction.
            for (int col = left; col <= right; col++) {
                result.add(matrix[up][col]);
            }
            // Top down direction
            for (int row = up + 1; row <= down; row++) {
                result.add(matrix[row][right]);
            }
            // Make sure we are on a different row
            if (up != down) {
                // Right to left direction
                for (int col = right - 1; col >= left; col--) {
                    result.add(matrix[down][col]);
                }
            }
            // Make sure we are on a different column
            if (left != right) {
                // Bottom up direction
                for (int row = down - 1; row > up; row--) {
                    result.add(matrix[row][left]);
                }
            }

            left++;
            right--;
            up++;
            down--;
        }

        return result;
    }
}
