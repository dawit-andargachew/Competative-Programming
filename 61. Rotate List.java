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
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null)
            return head;

        List<Integer> list = new ArrayList();
        while(head != null){
            list.add(head.val);
            head = head.next;
        }
        
        int len = list.size();
        int remainder = k % len;
        int rotate_point = len - remainder;

        ListNode node = new ListNode(0);
        ListNode rotate = node;
        
        // add elements after rotate point
        for(int i = rotate_point; i < len; i++){
            rotate.next = new ListNode(list.get(i));
            rotate = rotate.next;
        }

        // add elements before rotate point
        for(int i = 0; i < rotate_point; i++){
            rotate.next = new ListNode(list.get(i));
            rotate = rotate.next;
        }

        return node.next;
    }
}
