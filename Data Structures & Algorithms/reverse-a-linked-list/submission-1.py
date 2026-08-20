# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If List is empty or reach at last Node

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        # Make the next node point backward to current node.
        head.next.next = head

        head.next = None

        return new_head