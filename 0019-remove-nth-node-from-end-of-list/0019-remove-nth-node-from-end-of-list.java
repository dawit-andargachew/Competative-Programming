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
    public ListNode removeNthFromEnd(ListNode head, int n) {

   /** to remove the Nth elemnt we need to do,
        1, reverse the linked list
        2, store the elements until we got Nth element, lets use Store
        3, to remove Nth element, prev = prev.next
        4, finally, link Stored with prev, Stored.next = prev */

        // step 1, reverse the linked list, prev is head of reversed list
        ListNode prev = null;
        while(head != null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }

        //Step-2 store elements before the Nth-element,let use Store
        // and node points to head of store, node.next =>[head of Store]
        ListNode node = new ListNode(0);
        ListNode Store = node;
        while( n > 1){
            Store.next = new ListNode(prev.val);
            Store = Store.next;
            prev = prev.next;
            n--;
        }

        // Step-3, connect Store and prev after removing Nth-element
        // after (N-1) iteration, prev is the Nth element. so remove it
        prev = prev.next;// remove Nth element
        Store.next = prev; // connect Store and prev

        // get the head of the pointer, node.next => [points to head of Store]
        // Step-4, so to reverse the whole list after removing Nth element we need to grab the head 
        head = node.next;// grab head of the new list
        prev = null;

        // remove the list before we return
        while(head != null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }

        return prev;        
    }
}
