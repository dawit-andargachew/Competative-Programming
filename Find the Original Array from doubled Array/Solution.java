import java.util.HashMap;
import java.util.Arrays;

class Solution {

    public int[] findOriginalArray(int[] changed) {
        if (changed.length % 2 != 0) {
            return new int[] {};
        }

        Arrays.sort(changed);

        int size = changed.length;
        int[] res = new int[size / 2];
        int index = 0;

        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int j = size - 1; j >= 0; j--) {
            int element = changed[j];
            int twice = 2 * element;
            if (hashmap.containsKey(twice)) {
                if (hashmap.get(twice) == 1) {
                    hashmap.remove(twice);
                } else {
                    hashmap.put(twice, hashmap.get(twice) - 1);
                }
                res[index++] = element;
            } else {
                // !hashmap.containsKey(twice);
                hashmap.put(element, hashmap.getOrDefault(element, 0) + 1);
            }
        }
        return index == size / 2 ? res : new int[0];
    }
}