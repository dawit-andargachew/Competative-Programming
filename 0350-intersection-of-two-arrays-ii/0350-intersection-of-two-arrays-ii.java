class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        // tow get commmon elements with their respective frequencies lets use HashMap
        // store nums1 and nums2 with hashmap.
        // To get their common element and frequencies use another hashmap

        HashMap<Integer, Integer> one = new HashMap();// for nums1
        for(int i = 0; i < nums1.length; i++)
            one.put(nums1[i], one.getOrDefault(nums1[i], 0) + 1);
        
        HashMap<Integer,Integer> two = new HashMap();// for nums2
        for(int i = 0; i < nums2.length; i++)
            two.put(nums2[i], two.getOrDefault(nums2[i],0) + 1);

        HashMap<Integer,Integer> common = new HashMap();
        int common_amount = 0;// keep track of common size and used to creat array
        for(Map.Entry<Integer, Integer> set : one.entrySet()){ // to get their common element
            int k = set.getKey();
            int v = set.getValue();

            // common frequency is the minimum of the two,
            // like [2,2,2,2] and [2,2] => [2,2] is common with small frequency
            if(two.containsKey(k)){
                int min_frequency = Math.min(v, two.get(k));
                common_amount += min_frequency;
                common.put(k, min_frequency);
            }
        }   
  
        
        // we have hashmap but how do we copy to array
        // 1, use i for index and every time we add element increase its value
        // 2, store the frequency and decease it every time we add to array

        int[] arr = new int[common_amount];
        int i = 0;//controls index
        for(Map.Entry<Integer, Integer> set: common.entrySet()){

            int frequency = set.getValue();// control frequency
            while( frequency > 0){
                arr[i] = set.getKey();
                frequency--;
                i++;
            }
        }
        
        
        return arr;
    }
}