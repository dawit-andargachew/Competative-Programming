# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # lets use a heap, and heapify the array when ever we add a new element
        merged = []
        for head in lists:
            while head:
                heapq.heappush(merged, head.val)
                head = head.next

        dummy = ListNode()
        root = dummy
        while merged:
            temp = ListNode( heapq.heappop(merged) )
            root.next = temp
            root = temp

        return dummy.next