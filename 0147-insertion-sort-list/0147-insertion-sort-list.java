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
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode();

        while( head != null){
            ListNode temp = head.next;
            ListNode prev = dummy;
            ListNode nxt = dummy.next;
            while( nxt != null){
                if(nxt.val > head.val)
                    break;
                prev = nxt;
                nxt = nxt.next;
            }

            head.next = nxt;
            prev.next = head;
            head = temp;
        }

        return dummy.next;
    }
}