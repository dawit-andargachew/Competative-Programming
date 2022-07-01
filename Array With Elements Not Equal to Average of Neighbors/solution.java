class solution {
    boolean compare(int a, int b, int c) {
        return (((a + c) / 2) == b) ? true : false;
    }

    public int[] rearrangeArray(int[] nums) {

        boolean make_swap = true;
        while (make_swap) {
            make_swap = false;
            for (int i = 1; i < nums.length - 1; i++) {
                if (compare(nums[i - 1], nums[i], nums[i + 1])) {
                    int temp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = temp;
                    make_swap = true;

                }
            }
        }

        return nums;

    }
}