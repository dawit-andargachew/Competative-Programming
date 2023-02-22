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
    public int[] nextLargerNodes(ListNode head) {
        // here is a monotonic stack similar to 
        //      1475. Final Prices With a Special Discount in a Shop
        //      496. Next Greater Element I
        List<Integer> list = new ArrayList();        
        while( head != null){
            list.add(head.val);
            head = head.next;
        }
        
        int[] answer = new int[list.size()];
        Stack<Integer> stack = new Stack();
        
        for(int i = 0; i < list.size(); i++){
            
            while( stack.size() > 0 && list.get(stack.peek()) < list.get(i) )
                answer[stack.pop()] = list.get(i);
            
            stack.push(i);
        }
        
        return answer;        
    }
}