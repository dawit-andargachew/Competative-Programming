class one {
    static void sortColors(int[] nums) {
        int temp = 0;
        for (int i = 0; i <= nums.length - 2; i++) {
            for (int j = i + 1; j <= nums.length - 1; j++) {
                if (nums[i] > nums[j]) {
                    temp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = temp;
                }
            }
        }

        for (int i = 0; i < nums.length; i++)
            System.out.println(nums[i]);
    }
}