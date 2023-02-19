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

        // lets use stack 
        // step-1, when we get head.val < stack.peek()  => streactly decreasing add to stack
        // step-2, other wise remove all elements less than head.val and push(head.val)
        // step-3, copy elements of stack in to ListNode
            // it can handle [1,1,1,1] => all handled in step-2
            //      to be removed from stack it must be stack.peek() < head.val
            //      but 1 < 1 is false so only stack.push(1) is executed

        Stack<Integer> stack = new Stack();

        while(head != null){
            if(stack.size() > 0 && stack.peek() < head.val){// step-1
                while( stack.size() > 0 && stack.peek() < head.val)// step-2
                    stack.pop();

                stack.push(head.val);// append value after removing elements
            }else
                stack.push(head.val);

            head = head.next;
        }

        // step-3
       ListNode dummy = new ListNode();
       head = dummy;

       for(int i = 0; i < stack.size(); i++){
            head.next = new ListNode(stack.get(i));
            head = head.next;
        }

       return dummy.next;        
    }
}