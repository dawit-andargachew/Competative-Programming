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
  public ListNode swapPairs(ListNode head) {

    ListNode node = new ListNode(0);
    ListNode swap = node;

    // to swap adjacent values we need to use two different rule for even and odd length lined list

    // lets use 
    //      i => to keep track of index of each node
    //      previous => to hold the previous value of current node
    // 1, For odd length like this  6,7,8,9,10 => to 7,6,9,8,10
    //      if i is odd, make swap until head.next is null
    //             i == 1 for node value of 7 so swap [6,7]
    //             i == 3 for node value of 9 so swap [8,9] 
    //             10 is last node no swap, just put is as it is.
    //      finally we get 7,6,9,8,10

    // 2, For even length like 6,7,8,9 => to 7,6,9,8
    //      in addition to the above odd rules, we need to consider one thing
    //      i == 0 node value of 6
    //      i == 1 node value of 7, swap 6,7
    //      i == 2 node value of 8
    //      i == 3 node value of 9, next node is null so put is as it is.
    //          then we get 7,6,9 WHERE IS 8 ????????

    // So for even length, swap last node with it' previous
    //      How to check it is odd
    // i == 3 for node value 9 [for the above example]
    // i.e,  if( head.next == null && i&2 ==1){
    //            consider its previous node and make swap
    // finally we get  7,6,9,8

    int i = 0;// track the index
    int previous = 0;// track previous node value
    while (head != null) {

      if (head.next == null ) {
        swap.next = new ListNode(head.val);
        swap = swap.next;

        if( i%2 == 1){// make sure the lined-list is even length
        swap.next = new ListNode(previous);
        swap = swap.next;
        }

      } else if (i % 2 == 1) {
        // swap current node with is previous, Until next node is null [controlled by upper if conditon]
        swap.next = new ListNode(head.val);
        swap = swap.next;
        swap.next = new ListNode(previous);
        swap = swap.next;
      }

      previous = head.val;
      head = head.next;
      i++;
    }

    return node.next;
  }
}
