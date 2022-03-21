import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

class swapCount {
    public static void countSwaps(List<Integer> a) {

        int swapCounts = 0;
        for (int i = a.size() - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                if (a.get(j) > a.get(j + 1)) {
                    ++swapCounts;
                    Collections.swap(a, j + 1, j);// used to swap elements at a[j] and a[j+1] positions
                }
            }
        }

        System.out.println("Array is sorted in " + swapCounts + " swaps.");
        System.out.println("First Element: " + a.get(0));
        System.out.println("Last Element: " + a.get(a.size() - 1));
    }
}

class Bubble_Sort_SortCount {
    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>(); // sample list of integers
        a.add(12);
        a.add(1);
        a.add(55);
        a.add(99);
        a.add(3);
        swapCount.countSwaps(a); // swapCount call
    }

}