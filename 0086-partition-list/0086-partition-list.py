# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
      dummy = ListNode()
      lessThan = dummy

      # put all elements > x in lessThan
      # put all elements >= x in greateThan
      # then connect lessThan with greatThan
      greaterHead = ListNode()
      greaterThan = greaterHead

      #loop over the linkedlist and identify elements
      while head:
          if x > head.val:
              lessThan.next = ListNode(head.val)
              lessThan = lessThan.next            
          else:
              greaterThan.next = ListNode(head.val)
              greaterThan = greaterThan.next
          head = head.next

      # connecting lessThan with greaterThan
      lessThan.next = greaterHead.next
      return dummy.next