import java.util.Arrays;

class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);

        // Stores the final result
        int max_pairs = 0;

        // Initialize the left and right pointers
        int left = 0, right = nums.length - 1;

        // Traverse array until start < right
        while (left < right) {

            if (nums[left] + nums[right] > k)
                right--;

            else if (nums[left] + nums[right] < k)
                left++;

            else {
                left++;
                right--;
                max_pairs++;
            }
        }

        return max_pairs;
        
    }
}
