import java.util.Arrays;

class Solution {
    public int minIncrementForUnique(int[] nums) {
        Arrays.sort(nums);
        int moves = 0;

        // lets say int [] nums = { 2,2,2,2};
        // First of all, if < prev >= cur > , cur must be incremented < pre - cur + 1 > times to make the array unique.
        // Because we have sorted the array, so it is always true that -> < prev <= cur >.
        // But pre >= cur like [3,2] means first it was [2,2] then it becomes [3,2] when we try to make the array unique.
        // And here is sampel example and we show all neccessary steps, 
        // Let the given array is int[] nums = { 2,2,2,2};
        //   2,3,2,2 => move 1
        //   2,3,3,2 => move 2
        //   2,3,4,2 => move 3
        //   2,3,4,3 => move 4
        //   2,3,4,4 => move 5
        //   2,3,4,5 => move 6
        // the above can be implemented by using <diff> variable and store these 
        // values in <moves> variable such that < moves = moves + diff >
        // ------- BUT NOTE THIS
        // <diff> = difference + 1 => difference + to make unique
        // `2,2`,2,2 => diff = 0 + 1
        // 2,`3,2`,2 => diff = 1 + 1 => 2 because [1] for `3,3` makes equal and [1]for
        // `3,4` makes unique
        // 2,3,`4,2`=> diff = 2 + 1 => 3 because [2] for `4,4` makes equal and [1] for
        // `4,5,` makes unique
        //
        // And the code is here, for efficiency purppose I have removed <current> and <previous> variables
        //
        //      for (int i = 1; i < nums.length; i++) {
        //      int diff = 0;
        //      int previos = nums[i - 1];
        //      int current = nums[i];
        //      if (previos >= current) {
        //      diff = previos - current + 1;
        //      moves += diff;
        //      nums[i] += diff;
        //      }
        //      }

        for (int i = 1; i < nums.length; i++) {
            int diff = 0;

            if (nums[i - 1] >= nums[i]) {
                diff = nums[i - 1] - nums[i] + 1;
                moves += diff;
                nums[i] += diff;
            }
        }

        return moves;
    }
}
