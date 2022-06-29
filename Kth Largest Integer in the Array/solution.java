import java.math.BigInteger;
import java.util.Arrays;

class Solution {
    public String kthLargestNumber(String[] nums, int k) {
          BigInteger[] arr = new BigInteger[nums.length];
        for (int i = 0; i < nums.length; i++) {
            arr[i] = new BigInteger(nums[i]);
        }
        Arrays.sort(arr);
        return arr[nums.length - k ].toString();
    }

}