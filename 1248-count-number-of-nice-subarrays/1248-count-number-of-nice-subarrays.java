class Solution {
        public int numberOfSubarrays(int[] nums, int k) {
         
        // replace even by 0 and odd by 1 then this question becomes 560. Subarray Sum Equals K
        // We need to instantiate the map with map.put(0,1), Why?
        // lets take 1,1,2,1,1, == 1,1,0,1,1
        //      when we reach at the 3rd 1, sum - k == 0, But we don't have 0  on the map
        //      so we need to initialize with (0,1)
        //Replace all odd by 1 and even by 0
        for(int i=0;i<nums.length;i++)
            nums[i] = (nums[i] %2 == 0) ? 0 : 1;
        
        int count = 0;
        int sum = 0;

        HashMap<Integer, Integer> map = new HashMap();
        map.put(0,1);// initialize the hashMap

        int i =0;
        while(i < nums.length){
            sum += nums[i];
            if(map.containsKey(sum - k))// if sum -k found on the hashmap, add map.get(sum -k)
                    count += map.get(sum -k);

            map.put(sum, map.getOrDefault(sum, 0) + 1);
            i++;
        }


        return count;
    }
}