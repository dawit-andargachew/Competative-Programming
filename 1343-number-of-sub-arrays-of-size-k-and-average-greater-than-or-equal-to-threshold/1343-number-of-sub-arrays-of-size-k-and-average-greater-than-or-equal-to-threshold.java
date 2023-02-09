class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {

// OPTION I, OPTION II  is commented below this solution
        int count = 0;
        int sum = 0;
        for(int i = 0; i < k -1; i++)
            sum += arr[i];

        for(int i = 0; i < arr.length - k + 1; i++) {
            sum += arr[i+k -1];
            if (sum / k >= threshold)
                count++;
            
            sum -= arr[i];// decrease the sum
        }

        return count;
    }
}


// OPTION II
// class Solution {
//     public int numOfSubarrays(int[] arr, int k, int threshold) {

//         int count = 0;
//         int sum = 0;
//         int low = -1;

//         int i = 0;
//         while (i < arr.length) {
//             sum += arr[i];
//             if (i - low == k) {
//                 if (sum / k >= threshold)
//                     count++;

//                 i++;
//                 low++;// increase low pointer
//                 sum -= arr[low];// decrease the sum

//             } else
//                 i++;
//         }

//         return count;
//     }
// }