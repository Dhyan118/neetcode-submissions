# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        k = length - n

        if k == 0:
            return head.next

        temp = head

        for i in range(length - 1):
            if (i + 1) == k:
                temp.next = temp.next.next
                break

            temp = temp.next

        return head

