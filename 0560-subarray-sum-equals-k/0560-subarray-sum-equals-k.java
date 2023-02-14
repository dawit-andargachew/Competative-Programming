class Solution {
    public int subarraySum(int[] nums, int k) {
        // link - https://www.youtube.com/watch?v=XjP2mQr98WQ
        // here is a prefix sum problem and needs HashMap. Why? Lets see
        //case-1 sum == k , mean the sum of sub array is k so count++
        //case-2, use after getting the sum store in hashmap,
        //          if(sum - k) is found on the hashmap means
        //              int temp = sum - k  => there is a sub array where its sum is k
        // look this video  https://www.youtube.com/watch?v=XjP2mQr98WQ
        HashMap<Integer, Integer> map = new HashMap();

        int sum = 0;
        int count = 0;
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            if(sum == k)
                count++;
            if (map.containsKey(sum - k))
                count += map.get(sum - k);

            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }


        return count;        
    }
}