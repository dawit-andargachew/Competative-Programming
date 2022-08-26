import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int longestSubarray(int[] nums, int limit) {

        if (nums.length == 0)
            return 0;
        Deque<Integer> maxDq = new LinkedList<>();
        Deque<Integer> minDq = new LinkedList<>();

        int start = 0;
        int len = 0;
        for (int i = 0; i < nums.length; ++i) {
            while (!maxDq.isEmpty() && nums[i] > maxDq.peekLast())
                maxDq.pollLast();

            while (!minDq.isEmpty() && nums[i] < minDq.peekLast())
                minDq.pollLast();

            maxDq.add(nums[i]);
            minDq.add(nums[i]);

            if (maxDq.peekFirst() - minDq.peekFirst() > limit) {
                if (maxDq.peekFirst() == nums[start])
                    maxDq.pollFirst();

                if (minDq.peekFirst() == nums[start])
                    minDq.pollFirst();

                start++;
            }
            len = Math.max(len, i - start + 1);
        }
        return len;
    }
}