class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {


        int[] answer = new int[queries.length];
        int index = 0;
        for(int[] i : queries){
            int sum = arr[i[0]++];
            int start = i[0], end = i[1];
            while(start <= end)
               sum ^= arr[start++];

            answer[index++] = sum;
        }

        return answer;
    }
}