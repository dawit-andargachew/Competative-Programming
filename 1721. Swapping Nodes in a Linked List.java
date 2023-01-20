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
    public ListNode swapNodes(ListNode head, int k) {
        List<Integer> list = new ArrayList();

        // store all elements in list
        while(head != null){
            list.add(head.val);
            head = head.next;
        }

        // swap k and len() - k values
        int len = list.size();
        int temp = list.get(k-1);
        list.set(k-1, list.get(len - k));
        list.set(len - k, temp);

        ListNode node = new ListNode(0);
        ListNode swap = node;

        // put list values on the linked list
        for(int i = 0; i < len; i++){
            swap.next = new ListNode(list.get(i));
            swap = swap.next;
        }

    return node.next;        
    }
}
