class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        
        // for this one we can use hashMap too, but both arrays are sorted in increasing order
        // so why don't use only two pointers without hashmap
        // one = {2,3,5,8,9}
        // tow = {0,1,4,6,7,9} => the minimum common element is 9
        // case-1: if(one > two), 
        //           increase one pointer with one
        // case-2: if( two < one)
        //         increase two pointer with one

        int i = 0, j = 0;
        
        while(i < nums1.length && j < nums2.length){
            int one = nums1[i], two = nums2[j];
            if( one == two)// if equal return the value
                return one;
            else if( one < two)// increase nums1 pointer with one
                i++;
            else if( one > two)// increase nums2 pointer with one
                j++;
        }
        
        return -1;// no common minimum value is found
    }
}