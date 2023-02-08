class StockSpanner {
    Stack<int []> stack;
    // her is also anothe monotonic stack question, where the stack contains
    //        {price, its span}
    // every time we get price less than the current price 
    //      stack.push( new int [] {price, 1} )
    // else => the current price is greate than the peek
    //      so we need to sum up all days and store at the peek
    // lets assumlike this 
    // stack= {
    //      [20, 3]
    //      [30, 1]
    //      [50, 2]
    //     }
    // and consider three cases, 
    //      case 1: next is price is 10,
    //        stack = {
    //           [10, 1]
    //           [20, 3]
    //           [30, 1]
    //           [50, 2]
    //          }
    //      case 2: next is price is 40,
    //        stack = {
    //           [10, 1]
    //           [20, 3] //  1 + 3 + 1 + 1[ for 40] = 6
    //           [30, 1] // sum up all less than 40, stack = {
    //           [50, 2]                                 [40, 6]
    //        }                                          [50, 2] 
    //                                                     }
    //      case 3: next price is  60
    //        stack = {
    //           [40, 6] // sum up all 6 + 2 + 1 [for 60] = 9,  stack{
    //           [50, 2]                                         [60, 9]
    //          }                                                }

    public StockSpanner() {
        stack = new Stack();
    }
    
    public int next(int price) {
        int days = 1;
        while(stack.size() > 0 && stack.peek()[0] <= price)// it is greater than the peek() store there span
            days += stack.pop()[1];

        stack.push(new int[]{price,days});
        return days;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */


//  class StockSpanner {
//     // the question is stright forward, 
//     // The maximum number of days starting from the current day
//     // step-1; find the maximum number from the current day
//     // step-2: if(price < stock.get(i)) => break;
//     Stack < Integer > stock;
//     public StockSpanner() {
//         stock = new Stack();
//     }

//     public int next(int price) {
//         stock.push(price);
//         int count = 0;
//         for (int i = stock.size() - 1; i >= 0; i--) {
//             if (price >= stock.get(i))
//                 count++;
//             else if (price < stock.get(i))
//                 break;
//         }

//         return count;
//     }
// }

// /**
//  * Your StockSpanner object will be instantiated and called as such:
//  * StockSpanner obj = new StockSpanner();
//  * int param_1 = obj.next(price);
//  */