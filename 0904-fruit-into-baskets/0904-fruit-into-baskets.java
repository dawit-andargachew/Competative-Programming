class Solution {
    public int totalFruit(int[] fruits) {

        // The problem is fo find 
        //           the maximum substring length with only 2 integers

        //Here is a sliding windows problem, and we need to use hashmap to store these two and their frequency
        // case-1, if map.size() <= 1
        //          add new element to hashmap or increase its frequency
        // case-2, map.size() > 2
        //      remove all occurences unil the map.size == 1
        //      then add the new element with frequency of 1
        //
        
        // Both fruits[i] and fruits[j] are part of sliding windows, it is inclusive
        int count = Integer.MIN_VALUE;
        HashMap < Integer, Integer > map = new HashMap();

        int low = 0;
        int i = 0;
        while (i < fruits.length) {
            int n = fruits[i];
            // add new element or increase existing frequency b 1
            if (map.containsKey(n) ||  map.size() <= 1)
                map.put(n, map.getOrDefault(n, 0) + 1);

            // map.size() > 2 and there is new element fruits[i] to be addede
            else {
                // take 1,2,1,2,3
                // if fruits[i] == 3, the we need to remove [1,2,1] from the array "[1,2,1],2,3 "
                // so that hashmap.size() == 1 and there will be free space for '3'
                while (map.containsKey(fruits[low]) && map.size() != 1) {
                    map.put(fruits[low], map.get(fruits[low]) - 1);

                    if (map.get(fruits[low]) == 0)// if the frequency is zero remove from the hashmap
                        map.remove(fruits[low]);

                    low++;
                }

                map.put(n, 1);
            }

            // index i and j are part of sliding window, so i - j + 1, is the subarray  length
            count = Math.max(count, i - low + 1);
            i++;
        }

        return count;
    }
}