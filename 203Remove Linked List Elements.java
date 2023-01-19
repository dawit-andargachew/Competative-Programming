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
  public ListNode removeElements(ListNode head, int val) {
    ListNode node = new ListNode();
    ListNode no_duplicate = node;

    while (head != null) {
      if (head.val != val) {
        no_duplicate.next = new ListNode(head.val);
        no_duplicate = no_duplicate.next;
      }
      
      head = head.next;
    }
    return node.next;

  }
}
