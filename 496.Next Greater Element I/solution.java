import java.util.Arrays;
import java.util.List;

class solution {

    static int[] nextGreaterElement(int[] nums1, int[] nums2) {

        int[] answer = new int[nums1.length];

        List<Integer> list = Arrays.stream(nums2).boxed().toList();
        int index = 0;
        int value = 0;

        for (int i = 0; i < nums1.length; i++) {

            index = list.indexOf(Integer.valueOf(nums1[i]));

            // if the element is last, value = -1
            if (index == list.size() - 1)
                value = -1;

            // loop until we reach the last element
            while (index < list.size() - 1) {
                if (nums1[i] < list.get(index + 1)) {
                    value = list.get(index + 1);
                    break;
                } else
                    value = -1;

                index++;
            }

            answer[i] = value;
        }

        return answer;

    }

}