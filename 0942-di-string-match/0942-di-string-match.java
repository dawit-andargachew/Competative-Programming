class Solution {
    public int[] diStringMatch(String s) {
        // the question is you 
        //      when you get 'I', increase low by 1
        //      when you get 'D', decrease high by 1
        // finally since the array has n + 1 size 
        //      DI[size] = high or low because at the end both are equal

        int size = s.length();
        int low = 0;
        int high = size;
        
        int[] DI = new int[size + 1];

        for(int i = 0; i < size; i++){
            if( s.charAt(i) == 'I')
                DI[i] = low++;
            else
                DI[i] = high--;
        }
        
        DI[size] = low;// we can me either low or high

        return DI;        
    }
}