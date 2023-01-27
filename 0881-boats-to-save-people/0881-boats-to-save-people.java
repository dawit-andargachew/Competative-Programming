class Solution {
  public int numRescueBoats(int[] people, int limit) {
      // the boat can only carry at most 2 people.
      // Take their sum and consider these 2 casese [ and the array must be sorted]
      // case 1 if ( start + end > limit ) => need boat, end--
      // case 2 start + end <= limit => need boat, start ++, end--
    Arrays.sort(people); // sort
      
    int boats = 0;

    int start = 0, end = people.length - 1;
    while (start <= end) { //  '<=' makes sure the middle man also included 
                        // [ it may satisfy both conditions but at the end the number of boats increased by one ]
        if (people[start] + people[end] <= limit) {
            start++;
            end--;
         } else
             end--;

      boats++;
    }

    return boats;
  }
}