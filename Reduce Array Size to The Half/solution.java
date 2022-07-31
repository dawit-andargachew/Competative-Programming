import java.util.Arrays;
import java.util.HashMap;

class Solution {

    public static int minSize(int[] arr) {

        int len = arr.length;

        HashMap<Integer, Integer> freq = new HashMap<>();

        // frequency talble => storing the frequency along with the values
        for (int element : arr)
            freq.put(element, freq.getOrDefault(element, 0) + 1);

        // an array for storing the frequencies of each number
        int[] counting = new int[freq.values().size()];

        int index = 0;
        for (int fre : freq.values())
            counting[index++] = fre;

        Arrays.sort(counting);

        // to remove at least half of elements
        // we should start removing from the largest frequency
        // and do this until at least half of elements are removed
        // => store removed elements in a variable named 'removed'

        int answer = 0, removed = 0, half = len / 2;
        int i = counting.length - 1;
        while (removed < half) {
            answer++;
            removed = removed + counting[i--];
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] arr = { 9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19 };
        System.out.println(minSize(arr));
    }
}