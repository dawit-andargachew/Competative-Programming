import java.util.Arrays;
import java.util.Comparator;

class Solution {

    static class CompareString implements Comparator<String> {
        public int compare(String one, String two) {
            return (two + one).compareTo(one + two);
        }
    }

    public String largestNumber(int[] nums) {
        String[] nums_String = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            nums_String[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(nums_String, new CompareString());
        
        if (nums_String[0].equals("0"))
            return "0";
            
        String result= "";
        for (String numAsStr : nums_String) {
            result += numAsStr;
        }

        return result;
        
    }
}