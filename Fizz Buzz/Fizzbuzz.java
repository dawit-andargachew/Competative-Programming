import java.util.List;
import java.util.ArrayList;

class Fizzbuzz {
    class Solution {
        public List<String> fizz_Buzz(int n) {
            List<String> list = new ArrayList<>();
            int i = 1;
            while (i <= n) {
                if (i % 15 == 0)
                    list.add("FizzBuzz");
                else if (i % 3 == 0)
                    list.add("Fizz");
                else
                    list.add((i % 5 == 0) ? "Buzz" : Integer.toString(i));
                i++;

            }
            return list;
        }
    }
}