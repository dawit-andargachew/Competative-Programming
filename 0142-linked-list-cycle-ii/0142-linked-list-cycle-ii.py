# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return
        
        # lets uses Floyd's cycle detection algorithm
        slow, fast = head.next, head.next.next
        while slow and fast and fast.next:

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

            slow = slow.next
            fast = fast.next.next