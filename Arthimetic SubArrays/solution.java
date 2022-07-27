import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
          List<Boolean> retured_list = new ArrayList<Boolean>();
        int check = 0;
        // int size =
        for (int i = 0; i < r.length; i++) {
            int[] part = Arrays.copyOfRange(nums, l[i], r[i] + 1);

            Arrays.sort(part);
            
            int difference = part[1] - part[0];
            for (int j = 0; j < part.length - 1; j++) {
                if (part[j + 1] - part[j] != difference)
                    check++;
            }

            if (check == 0)
                retured_list.add(true);
            else
                retured_list.add(false);
            check = 0;

        }
        return retured_list;

        
    }
}