class Solution {
    public int pivotInteger(int n) {
        // here is similar to 724. Find Pivot Index and 1991 Find the Middle Index in Array
        // The only difference is the pivot number is added to both left and right sums
        // leftSum => leftSum += i 
        // rightSum => total - leftSum + i, because pivot index is inclusive

        int total = 0;
        for(int i =0; i <= n; i++)
            total += i;

        int i = 1;
        int leftSum = 0;
        /// stores the sum of numbers starting from  i = 1 to pivot index
        // since the pivot number is included in both sums add i to letfSum and rightSum
        while(i <= n){
            leftSum += i;// before comparig with rightSum, add i to leftSum b/ce i is inclusive

            if(total - leftSum + i == leftSum)// compare it with right Sum including i
                return i;
            else
                i++;
        }

        return -1;        
    }
}
