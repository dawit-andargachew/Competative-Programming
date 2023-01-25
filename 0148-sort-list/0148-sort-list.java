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
  public ListNode sortList(ListNode head) {
    if (head == null || head.next == null)
      return head;
  
    ListNode dummy = new ListNode();
    ListNode node = dummy;
    // lets consider 3 cases [basically, it a merge sort problem]
    // case1 head.val >= node.val => append at the last
    // case 2 head.val <= dummy.next => append at the first
    // case 3 the element is in between and nees a little explanation
    //          prev = holds previous node
    //          top = dummy.next, top element of ordered linkedlist
    //          then check for each value and re-wire like this
    //                      prev.next = newNode;
    //                      newNode.next = top;



    // lets create the new ordered linkedlist with the first element
    node.next = new ListNode(head.val);
    node = node.next;
    head = head.next;// move head forward

    while (head != null) {

      ListNode newNode = new ListNode(head.val);
      ListNode top = dummy.next;

      if (newNode.val >= node.val) { // case 1
        node.next = newNode;
        node = node.next;
      } else if (newNode.val <= top.val) { // case 2
        newNode.next = top;
        dummy.next = newNode;
      } 
      else {// case -3

        while (top.next != null) {
          if (newNode.val <= top.next.val) {// re-wire the nodes 
            newNode.next = top.next;
            top.next = newNode;
            break;
          }
          top = top.next;
        }

      }
      head = head.next;
    }


    return dummy.next;
  }
}


//// solution by copying values on to arraylist
// class Solution {
//   public ListNode sortList(ListNode head) {
//     if (head == null || head.next == null)
//       return head;

//     List < Integer > list = new ArrayList();
//     while (head != null) {
//       list.add(head.val);
//       head = head.next;
//     }

//     Collections.sort(list);

//     ListNode node = new ListNode(0);
//     head = node;

//     for (int i = 0; i < list.size(); i++) {
//       head.next = new ListNode(list.get(i));
//       head = head.next;
//     }

//     return node.next;
//   }
// }