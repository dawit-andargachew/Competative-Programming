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
    public boolean isPalindrome(ListNode head) {
        // if it has only one element, it is palindrom
        // if the list has more than one elmenet copy the values in list and check 
        // whether the it is palindrom or not

        if(head.next == null)
            return true;

        List<Integer> list = new ArrayList();

        while(head != null){
            list.add(head.val);
            head = head.next;
        }

        int start = 0, end = list.size() - 1;

        while(start < end){
            if(list.get(start) != list.get(end))
                return false;
            start++;
            end--;
        }

        return true;        
    }
}
