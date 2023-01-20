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
  public ListNode deleteMiddle(ListNode head) {
    List < Integer > nums = new ArrayList();
    while (head != null) {
        nums.add(head.val);
        head = head.next;
      }

      int mid = nums.size()/2; 
      nums.remove(mid);
    //   System.out.println(nums.get(mid));

      ListNode node = new ListNode(0);
      ListNode list = node;

      for (int i = 0; i < nums.size(); i++) {
        list.next = new ListNode(nums.get(i));
        list = list.next;
      }

      return node.next;
    }
  }