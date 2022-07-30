import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class solution {

    private HashMap<Integer, Integer> sortByValue(Map<Integer, Integer> map) {
        // Create a list from elements of HashMap
        List<Map.Entry<Integer, Integer>> sortedMap = new LinkedList<Map.Entry<Integer, Integer>>(map.entrySet());

        // Sort the list
        Collections.sort(sortedMap, new Comparator<Map.Entry<Integer, Integer>>() {
            public int compare(Map.Entry<Integer, Integer> o1,
                    Map.Entry<Integer, Integer> o2) {
                return (o1.getValue()).compareTo(o2.getValue());
            }
        });

        HashMap<Integer, Integer> temp = new LinkedHashMap<Integer, Integer>();
        for (Map.Entry<Integer, Integer> aa : sortedMap) {
            temp.put(aa.getKey(), aa.getValue());
        }
        return temp;
    }

    public int[] topKFrequent(int[] nums, int k) {

        // holds the frequency of each number
        Map<Integer, Integer> frequency = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (frequency.containsKey(nums[i]))
                frequency.put(nums[i], frequency.get(nums[i]) + 1);
            else
                frequency.put(nums[i], 1);
        }

        // the map becomes sorted by value,
        Map<Integer, Integer> sortedFrequency = sortByValue(frequency);

        // pick key values from the map => NB => keys are unique with in the map
        ArrayList<Integer> key_list = new ArrayList<>(sortedFrequency.keySet());

        // int[] ints = Arrays.stream(value_list).mapToInt(o -> (int) o).toArray();
        // convert key_list to array
        int[] arr = key_list.stream().mapToInt(Integer::intValue).toArray();

        // select the last k elements which have high frequency
        arr = Arrays.copyOfRange(arr, arr.length - k, arr.length);

        // sort the array before we return
        Arrays.sort(arr);
        return arr;
    }

}