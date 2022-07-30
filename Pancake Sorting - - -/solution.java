import java.util.ArrayList;
import java.util.List;

class solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> res = new ArrayList<>();
        for (int x = A.length, i; x > 0; x--) {
            for (i = 0; A[i] != x; i++);  // do no forget this semi colon

            reverse(A, i + 1);
            res.add(i + 1);
            reverse(A, x);
            res.add(x);
        }
        return res;
    }

    public void reverse(int[] A, int k) {
        int j = k - 1;
        for (int i = 0; i < j; i++) {
            int tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
            j--;
        }
    }
}