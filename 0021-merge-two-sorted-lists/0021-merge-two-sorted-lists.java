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
  public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    ListNode a = new ListNode();
    ListNode total = a;

    while (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        total.next = new ListNode(list1.val);
        total = total.next;
        list1 = list1.next;
      } else if (list1.val > list2.val) {
        total.next = new ListNode(list2.val);
        total = total.next;
        list2 = list2.next;
      } else { // if they are equal
        total.next = new ListNode(list1.val);
        total = total.next;
        list1 = list1.next;

        total.next = new ListNode(list2.val);
        total = total.next;
        list2 = list2.next;
      }
    }

    //both fo while loops handle, if the length of list1 and list2 is not equal
    // or if one of them is contains values less than the other we need to merge those values
    while (list1 != null) { 
      total.next = new ListNode(list1.val);
      total = total.next;
      list1 = list1.next;
    }

    while (list2 != null) {
      total.next = new ListNode(list2.val);
      total = total.next;
      list2 = list2.next;
    }

    return a.next;
  }
}