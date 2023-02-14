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
    public ListNode[] splitListToParts(ListNode head, int k) {
        // the maximum number of nodes is  1000, so lets use int array 
        // how to determine the number of elements in each row?
        //       length = 11 and k = 3, remainder = 2
        //          [0] = 1,2,3,4 -> k + 1
        //          [1] = 1,2,3,4 -> k + 1
        //          [2] = 1,2,3
        //      because no two parts should have a length more than 1,
        //      to control this `remainder, the first 'r' elements have additional one element` is used, where 'r' == remainder
        
        
        // copy elements to array
        int len = 0;
        int[] nums = new int[1001];// 0 to 1000 => 1001 elements
        while (head != null) {
            nums[len++] = head.val;
            head = head.next;
        }

        
        int row_length = len / k; // determines the size of each individual row
        int remainder = len % k; // the first 'm' elements will have additional '1' elements, where m == remainder

        ListNode[] split = new ListNode[k];// create array of ListNode
        int row_index = 0; // controls the row index for ListNode array split
        int i = 0;// used to acess nums array
        while (i < len) {

            int sub_array_length = row_length;
            if (remainder--> 0) // remainder > 0 => means the current row size is k + 1
                sub_array_length++;

            ListNode dummy = new ListNode();
            ListNode node = dummy;
            while (sub_array_length > 0) {// add sub_array_length elements to the linked list
                node.next = new ListNode(nums[i++]);
                node = node.next;
                sub_array_length--;
            }

            split[row_index++] = dummy.next;// put the head of a linked list on the row
        }

        return split;
    }
}