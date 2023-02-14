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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        // lets use two stacks and store each values first
        // then start from a new ListNode, But the new node holds a default value when it is created,
        // So how do remove it 
        // apply this
        //      
        //      ListNode head = new ListNode() // head = 5       
        //      ListNode temp = new ListNode(sum); // temp = 5

        //       temp.next = head.next; // temp -> head
        //       head.next = temp; // head -> temp
        //      so head.next => points to add of the two numbers

        Stack<Integer> one = new Stack();
        while( l1 != null){
            one.push(l1.val);
            l1 = l1.next;
        }

        Stack<Integer> two = new Stack();
        while( l2 != null){
            two.push(l2.val);
            l2 = l2.next;
        }

        ListNode head = new ListNode();
        int remainder = 0;
        // since It needs the remainder, check weather the remainder zeros or not
        // like addding 9,9,9,9 + 1 => needs remanider to be checked
        while( one.size() > 0 || two.size() > 0 || remainder != 0){
            int sum = 0;            
            if(one.size() > 0) sum = one.pop();
            if(two.size() > 0) sum += two.pop();

            sum += remainder;

            remainder = sum/ 10;
            sum = sum % 10;

            ListNode temp = new ListNode(sum);

            temp.next = head.next;
            head.next = temp;
        }

        return head.next;
    }
}