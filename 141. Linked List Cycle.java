/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        List<ListNode> list = new ArrayList();

        while(head != null){
            if(list.contains(head))// it is strait forward, if it has the node previously stored it has cycle
                return true;

            list.add(head);
            head = head.next;
        }

        return false;        
    }
}
