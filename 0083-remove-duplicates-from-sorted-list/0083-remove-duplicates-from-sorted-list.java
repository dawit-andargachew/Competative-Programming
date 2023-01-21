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
        List<Integer> nums = new ArrayList();

        while(head != null){
            if(!nums.contains(head.val))
                nums.add(head.val);
            head = head.next;
        }

        ListNode node = new ListNode(0);
        head = node;
        for(int i = 0; i < nums.size(); i++){
            head.next = new ListNode(nums.get(i));
            head = head.next;
        }

        return node.next;        
    }
}