import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class solution {
    static String reverseParentheses(String s) {

        List<Character> one = new ArrayList<>();
        Queue<Character> queue = new LinkedList<>();
        for (char c : s.toCharArray())
            one.add(c);

        try {
            for (int i = 0; i < one.size(); i++) {

                if (one.get(i) == ')') {
                    int j = i - 1;

                    one.set(i, '|');// replace )

                    while (one.get(j) != '(') {
                        queue.add(one.get(j));
                        j--;
                    }
                    one.set(j, '|'); // remove (

                    j++;
                    while (!queue.isEmpty()) {
                        one.set(j, queue.poll());
                        j++;
                    }
                }
            }

        } catch (Exception e) {
        }

        // one.removeIf(x -> x == '|');
        // [|, ] <- is regx and mathces any of the characters between [],
        // here we want to remove | comma and white-space from the list called one
        // \\[ and \\] <- add ] adn [ in the regx
        String result = one.toString().replaceAll("[|,\\[\\] ]", "");

        return result;

    }
}