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
  public int pairSum(ListNode head) {
    // store the numbers in list
    List < Integer > num = new ArrayList();
    while (head != null) {
      num.add(head.val);
      head = head.next;
    }

    int start = 0, end = num.size() - 1;
    int twin_sum = Integer.MIN_VALUE;

    // add twin paris and compare their sum with the previous one
    while (start < end) {
      int temp = num.get(start) + num.get(end);
      twin_sum = Math.max(twin_sum, temp);
      start++;
      end--;
    }

    return twin_sum;
  }
}
