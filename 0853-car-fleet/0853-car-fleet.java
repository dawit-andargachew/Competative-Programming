class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        
        
        Stack<Float> stack = new Stack();
        int[][] ordered = new int[position.length][2];
        for(int i =0; i< position.length;i++){
            ordered[i][0] = position[i];
            ordered[i][1] = speed[i];
        }

        Arrays.sort(ordered,(a,b)->a[0]-b[0]);

        for(int i = 0; i < ordered.length; i++) {
            float time = (float)(target - ordered[i][0])/ordered[i][1];
            
            while(stack.size() > 0 && stack.peek() <= time)
                stack.pop();
            
            stack.push(time);            
        }      
        
        return stack.size();
    }
}