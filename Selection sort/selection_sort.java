class solution {
    static int[] selection_sort(int array[]) {
        int mid, temp;
        for (int i = 0; i < array.length - 1; i++) {

            mid = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] > array[j]) {
                    mid = j;

                    if (i != mid) {
                        temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
            }
        }
        return array;
    }
}
