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
            // remove the last element until nums[i] is greater or equal
            while (!maxDq.isEmpty() && nums[i] > maxDq.peekLast())
                maxDq.pollLast();
            
            // remove the last element until nums[i] is greater or equal
            while (!minDq.isEmpty() && nums[i] < minDq.peekLast())
                minDq.pollLast();

            maxDq.add(nums[i]);
            minDq.add(nums[i]);

            if (maxDq.peekFirst() - minDq.peekFirst() > limit) {
                // when we increase the start pointer we should remove the first element inserted in the dequeue
                if (maxDq.peekFirst() == nums[start])
                    maxDq.pollFirst();

                // when we increase the start pointer we should remove the first element inserted in the dequeue
                if (minDq.peekFirst() == nums[start])
                    minDq.pollFirst();

                start++;
            }
            
            len = Math.max(len, i - start + 1);
        }
        return len;
    }
}
