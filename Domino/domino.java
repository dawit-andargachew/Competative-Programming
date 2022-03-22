
class domino_pilling {
    static int pilling(int n, int m) {
        return m * n / 2;
    }
}

public class domino {
    public static void main(String[] args) {
        System.out.println(domino_pilling.pilling(3, 3));
    }
}