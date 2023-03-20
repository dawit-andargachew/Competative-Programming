import java.io.*;
import java.math.*;
import java.security.*;
import java.util.Collections;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'countSwaps' function below.
     *
     * The function accepts INTEGER_ARRAY a as parameter.
     */

      public static void countSwaps(List<Integer> a) {

        int swapCounts = 0;
        for (int i = a.size() - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                if (a.get(j) > a.get(j + 1)) {
                    ++swapCounts;
                    Collections.swap(a, j + 1, j);
                }
            }
        }

        System.out.println("Array is sorted in " + swapCounts + " swaps.");
        System.out.println("First Element: " + a.get(0));
        System.out.println("Last Element: " + a.get(a.size() - 1));
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> a = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.countSwaps(a);

        bufferedReader.close();
    }
}
