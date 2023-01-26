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

// class Solution {
//     public void reorderList(ListNode head) {
//         if( head.next == null)
//             return;
        
//         List<Integer> list = new ArrayList();
        
//         while( head != null){
//             list.add(head.val);            
//             head = head.next;
//         }
        
        
//         ListNode dummy = new ListNode();
//         ListNode node = dummy;
        
//         int size = list.size();
//         int start = 0, end = size - 1;
        
//         while( start < end ){
//             node.next = new ListNode(list.get(start));
//             node = node.next;
            
//             node.next = new ListNode(list.get(end));
//             node = node.next;
            
//             start++;
//             end--;
//         }
        
//         if(size%2 == 1){
//             node.next = new ListNode(list.get(size/2));
//             node = node.next;
//         }
        
//         head = dummy.next;
        
//     }
// }
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
    
    public ListNode reverse(ListNode head2){
        ListNode cur=head2;
        ListNode prev=null;
        while(cur!=null){
            ListNode temp=cur.next;
            cur.next=prev;
            prev=cur;
            cur=temp;
        }
        return prev;
    }

    public void reorderList(ListNode head) {
        ListNode slow=head;
        ListNode fast=head;

        //for finding the  middle
        while(fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;
        }

        //we are simply dividing the linkedList
        ListNode first=head;
        ListNode second=reverse(slow.next);//reverse the second linkedlist
        slow.next=null;

        //we are running the while loop until second is null,
        //beacuse second linked list length will be always <= first's length
        while(second!=null){
            //merging the two linked list 
            ListNode temp1=first.next;
            first.next=second;
            ListNode temp2=second.next;
            second.next=temp1;
            first=temp1;
            second=temp2;
        }
    }
}