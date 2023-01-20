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
    public ListNode mergeNodes(ListNode head) {

        // node.next => points to head of merged,and it keeps the merged list to be returned
        ListNode node = new ListNode(0);
        ListNode merge = node;

        // removes the first 0, and prevents from adding 0 in the head of merged list
        head = head.next;
        while( head != null){
            int sum = 0;
        
            // loops until we get 0, add  store their sum
            while(head != null && head.val != 0){
                sum += head.val;
                head = head.next;
            }

            // create a list and make a chain
            merge.next = new ListNode(sum);
            merge = merge.next;

            head = head.next; // moves to the next non-zero nodes, or finally head = null and it terminates
        }

        return node.next;        
    }
}
