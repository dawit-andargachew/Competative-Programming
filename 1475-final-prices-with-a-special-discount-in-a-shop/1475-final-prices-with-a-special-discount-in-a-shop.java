class Solution {
    public int[] finalPrices(int[] prices) {
        // to make sure the discount is offered lets use a boolean variable and
        // if it is not offered, put its value as it is
        
        int len = prices.length;
        int[] discount = new int[len];
        
        for(int i  = 0; i < len; i++){
            
            int j = i + 1;
            boolean isDiscount = true;
            while( j < len){ // loop until we get the discout offer
                if( prices[j] <= prices[i]){
                    discount[i] = prices[i] - prices[j];
                    isDiscount = false;
                    break;
                }
                
                j++;
            }
            
            if(isDiscount)// no discount, put the value as it is
                discount[i] = prices[i];
        }
            
        return discount;        
    }
}