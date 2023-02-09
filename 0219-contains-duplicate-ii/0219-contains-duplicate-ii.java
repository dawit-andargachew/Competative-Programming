class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {

        // the question is to find duplicates where there indices i - j <= k
        // so lets use hashmap and store there indices


        HashMap<Integer, Integer> map = new HashMap();

        for(int i =0; i < nums.length; i++){
            int n = nums[i];

            // whenever we get duplicate and i - map.get(n) <= k return true
            if(map.size() > 0 && map.containsKey(n) && i - map.get(n) <= k)
                return true;
            else
                map.put(n, i);
        }
        
        return false;
    }
}