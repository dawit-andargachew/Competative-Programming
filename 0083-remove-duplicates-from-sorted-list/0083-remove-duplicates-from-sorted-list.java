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
    public ListNode deleteDuplicates(ListNode head) {
       if(head == null || head.next == null)
            return head;
        
        
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        
        node.next = new ListNode(head.val);
        node = node.next;
        head = head.next;
        
        while(head != null){
            
            if(head.val != node.val){
                node.next = new ListNode(head.val);
                node = node.next;
            }                    

            head = head.next;
        }
        
        return dummy.next;       
        
    }
}