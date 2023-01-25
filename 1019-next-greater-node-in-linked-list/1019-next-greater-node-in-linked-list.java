/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public int[] nextLargerNodes(ListNode head) {
     // lets use two Stacks Key and value, K stores each element and V holds the next greater value
     // Step-1 if head.val >= head.next.val, it is not strictly increasing so store (head.val, 0)
     // Step-2, head.val < head.next.val, it is strictly increasing 
     //    and we need to check whether it is the next greater element for previos elements l
     //    like [1,7,3,2,1,5] => (1,3),(3,0),(2,0)
     //     after we get 5 it becomes the next greter element for 3 and 2 as well [not for (1,7) it has next greater element]
     //   so traverse backward and 
     ///       1, if(K.get(i) > head.val) =>  head.val is not greater element for this and all the previos values found before it
     //                   take (1,7,3,2,1,5), 5 is greaer element for 3,2,1 but not for 1,7
     //                   because 7 > 5 => 5 is not greater element for 7 and previos elements of 7 i.e, [1,7]
     //       2, else if(V.get(i) == 0) => head.val is greater element
     //                        take (1,7,3,2,1,5),  for 3,2 have no greater element [and are less than 5]
     //                          if they were like 8 or 9 => (1,7,8,3,2,1,5) [ gteater than 5], the above condition break the loop
     // Step-3 if (head.next == null) => have no greaer element so make 0 [ for last elements]

    Stack < Integer > K = new Stack();
    Stack < Integer > V = new Stack();
    while (head != null) {

      if (head.next != null && head.val >= head.next.val) { // step-1 Not strictly increasing
        K.add(head.val);
        V.add(0);

      } else if (head.next != null && head.val < head.next.val) { // step-2 is strictly increasing

        // traverse backward and check it is their next greater element
        for (int i = K.size() - 1; i >= 0; i--) {
          if (K.get(i) >= head.next.val)
            break;

          if (V.get(i) == 0)// if is is zero they have no greater element, but if not zero they have next greater element
            V.set(i, head.next.val);
        }

        K.add(head.val);
        V.add(head.next.val);

      } else if (head.next == null) {// step-3 next element is null
        K.add(head.val);
        V.add(0);
      }

      head = head.next;
    }

    //array to be returned
    int[] nums = new int[V.size()];
    for (int i = 0; i < V.size(); i++)
      nums[i] = V.get(i);

    return nums;
  }
}