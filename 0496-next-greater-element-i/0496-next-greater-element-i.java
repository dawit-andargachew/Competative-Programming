class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        // it is the same as 1475. Final Prices With a Special Discount in a Shop
        // each values of nums1 are  unique so we can store their index in hashmap
        // the we iterate though the second array nums2,

        // stack contains decreasing elements [4,2,]...
        // when we get larger element than the stack.peek(), use the index stored on hashmap and put the greater element

        HashMap<Integer, Integer> map = new HashMap();
        for(int i = 0; i < nums1.length; i++)
            map.put(nums1[i], i);

        int[] next = new int[nums1.length];
        Arrays.fill(next, - 1);// set defaul value of -1

        Stack<Integer> stack = new Stack();
        for(int i = 0; i < nums2.length; i++ ){
            
            int n = nums2[i];
            while( stack.size() > 0 && n  > stack.peek())// put next greater element
                next[map.get(stack.pop())] = n;

            if(map.containsKey(n))
                stack.add(n);
        }

        return next;        
    }
}