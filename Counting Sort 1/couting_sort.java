import java.util.*;

class couting_sort {

    public static List<Integer> countingSort(List<Integer> arr) { 
        List<Integer> result = new ArrayList<>();

        int max = 0;

        // find the largetst value
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > max)
                max = arr.get(i);
        }

        // initialize the result array
        for (int i = 0; i <= max; i++)
            result.add(0);

        for (int i = 0; i < arr.size(); i++) {
            int temp = arr.get(i); // temp =1
            result.set(temp, (result.get(temp) + 1));
        }

        return result;
    }

}
