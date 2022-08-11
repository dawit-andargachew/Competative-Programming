class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode result = new ListNode(0);
        ListNode prev = result; 

        while (head != null) {
            ListNode next = head.next; 
            if (prev.val >= head.val)
                prev = result; 
            while (prev.next != null && prev.next.val < head.val)
                prev = prev.next;
            head.next = prev.next;
            prev.next = head;
            head = next; 
        }

        return result.next;
    }
}