import java.util.ArrayList;
import java.util.List;

class Grading {
    public static List<Integer> gradingStudents(List<Integer> grades) {

        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < grades.size(); i++) {
            if (grades.get(i) >= 38) {
                int remainder = grades.get(i) / 5;
                int difference = (remainder + 1) * 5 - grades.get(i);
                if (difference < 3) {
                    int value = (remainder + 1) * 5;
                    result.add(i, value);
                } else
                    result.add(grades.get(i));

            } else
                result.add(grades.get(i));
        }
        return result;
    }
}
