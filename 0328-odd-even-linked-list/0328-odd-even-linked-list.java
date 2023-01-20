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
    public ListNode oddEvenList(ListNode head) {
        
        // store even node numbers
        List<Integer> even = new ArrayList();

        ListNode answer = new ListNode(0);
        ListNode list = answer;
        
        int index = 1;
        while(head != null){
            if(index % 2 == 1){
                list.next = new ListNode(head.val);
                list = list.next;
            }else 
                even.add(head.val);

            head = head.next;
            index++;
        }

        // add even nodes 
        for(int i = 0; i < even.size(); i++){
            list.next = new ListNode(even.get(i));
            list = list.next;
        }

        return answer.next;       
        
    }
}