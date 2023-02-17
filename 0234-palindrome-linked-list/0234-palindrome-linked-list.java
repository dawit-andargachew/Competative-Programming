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
        // Let's reverse the linked list and  [copy its element to another list]
        // riversing a linkedlist like below [ doesn't create another linkedlist] 
        // so we need to it copy for latter comparison

        ListNode dummy = new ListNode();
        ListNode original = dummy;
        ListNode prev = null;

        while( head != null){
            original.next = new ListNode(head.val);// create another linkedlist for later comparison
            original = original.next;

            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }

        original = dummy.next; 
        while( prev != null && original != null){// compare original and reversed lists
            if( prev.val != original.val)
                return false;
            prev = prev.next;
            original = original.next;
        }

        return true;
    }
}


// copying all the elements on Arraylist and check whether it is a palindrom or not
// class Solution {
//     public boolean isPalindrome(ListNode head) {
//         // if it has only one element, it is palindrom
//         // if the list has more than one elmenet copy the values in list and check 
//         // whether the it is palindrom or not

//         if(head.next == null)
//             return true;

//         List<Integer> list = new ArrayList();

//         while(head != null){
//             list.add(head.val);
//             head = head.next;
//         }

//         int start = 0, end = list.size() - 1;

//         while(start < end){
//             if(list.get(start) != list.get(end))
//                 return false;
//             start++;
//             end--;
//         }

//         return true;        
//     }
// }