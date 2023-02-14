class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        // The goal is too get where does the chalk ends???
        //      the easiest way is k = k - chalk[i], until k reaches zero,
        //      But is not optimized, the time complexity becomes large for large k values
        //
        // Why don't  we sum up all the chalks needed by students, chalk[i] {because the goal is substract chalk[i] to k}
        //      the simplest way is get the module, k = k % sum
        //      then iterate it and get the index when chalk[i] > k becomes true
        
        double sum = 0;/// there sum becomes too large so using large space is better
        for(int i: chalk)
            sum += i;
        k =(int)( k % sum);

        int i =0;
        while(i < chalk.length){
            if(chalk[i] > k)//
                return i;
            
            k -=  chalk[i++];
        }

        return 4444; // just for formality       
    }
}