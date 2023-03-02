class Solution {
    public int fib(int n) {
        
    if( n == 0)
        return 0;
    else if( n == 1)
        return 1;
        
       int[] num = new int[n+1];
        num[1] = 1;
        
        int i  = 2;
        while( i <= n){
            num[i] = num[i-1] + num[i-2];            
            i++;
        }
        
        return num[n];
    }
}