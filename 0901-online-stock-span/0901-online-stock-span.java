class StockSpanner {
    // the question is stright forward, 
    // The maximum number of days starting from the current day
    // step-1; find the maximum number from the current day
    // step-2: if(price < stock.get(i)) => break;
    
  List < Integer > stock;// store the prices
  public StockSpanner() {
    stock = new ArrayList();
  }

  public int next(int price) {
      
    stock.add(price);
    int count = 0;// store maximum number of concecutive days
    for (int i = stock.size() - 1; i >= 0; i--) {
      if (price >= stock.get(i))
        count++;
      else if (price < stock.get(i))
        break;
    }

    return count;
  }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */