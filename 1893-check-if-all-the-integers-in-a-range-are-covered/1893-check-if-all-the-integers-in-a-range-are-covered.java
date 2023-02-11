class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
    
    // to check whether the range is covered or not, let sort the array first
    // the code works like this,
    // take [[1,4],[9,12],[15,26]] and left = 3, right = 11 must
    //          be return false because 5,6,7,8 is not covered
    //        first sort  [[1,4],[9,12],[15,26]]
    // then check this   if(left >= ranges[i][0] && left <= ranges[i][1])
    //                      and make left = ranges[i][1] + 1
    // If there is any jump or any element is not coverd the left will never greater than zero
    //
       Arrays.sort(ranges, (x,y)->x[0]-y[0]);
        for(int i = 0; i < ranges.length; i++)
        // compare left to both ends of a given range
            if(left >= ranges[i][0] && left <= ranges[i][1])
                left = ranges[i][1] + 1;

    return left > right;        
    }
}