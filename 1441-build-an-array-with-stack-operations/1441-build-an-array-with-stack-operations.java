class Solution {
    public List<String> buildArray(int[] target, int n) {
        
        // the goal is simply create array of push and pop given that 
        //   - target, and
        //   - array of numbers from 1 to n incusive [lets this with j]
        // Teh solution is 
        //step-1 if(target [i] == j) => list.add("push"), i++ and j++
        //step-2, if(target[i] != j)=> list.add("push"), list.add('pop'), j++

        
        int j = 1;
        List<String> list = new ArrayList();
        for(int i = 0; i < target.length && j <= n; ){
            if( target[i] == j){// if they are equal,
                list.add("Push");
                i++;
                j++;
            } else {// step-2, they are not equal
                list.add("Push");
                list.add("Pop");
                j++;
            }   
        }
        
        return list;     
    }
}