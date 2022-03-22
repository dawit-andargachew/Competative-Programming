class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
              List<Integer> output = new ArrayList<>();
        int temp;
        // sorting the array
        for (int i = 0; i <= nums.length - 2; i++) {
            for (int j = i + 1; j <= nums.length - 1; j++) {
                if (nums[i] > nums[j]) {
                    temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }

        // selecting target indices
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target)
                output.add(i);
        }
        return output;
    }
}