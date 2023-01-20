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
    public ListNode removeNodes(ListNode head) {

        ListNode node =new ListNode(0);
        ListNode list = node;

        int later = 0;
        boolean isequal = true;

        // holds the first element and check if all of nodes have equal value,
        // like 1,1,1,1,1 so no need to remove element
        if(head.next != null && head.val == head.next.val){
            later = head.val;
        }


        while( head != null){

            if(head.next != null && head.val <= head.next.val){
                list.next = new ListNode(head.next.val);
                list =  list.next;
            }
            if( later != head.val)
                isequal = false;
            head = head.next;
        }

        if(isequal){
            list.next = new ListNode(later);
            list =  list.next;

        }


        return node.next;        
    }
}
