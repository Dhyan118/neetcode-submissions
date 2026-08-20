# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Finnd the mid value

        h1 = head
        h2 = slow.next 
        slow.next = None

        #reverse the Linkedlist

        prev = None
        while h2:
            temp = h2.next
            h2.next = prev
            prev = h2
            h2 = temp

        h2 = prev

        #Merge the Linkedlist

        while h2:
            temp1 = h1.next
            temp2 = h2.next

            h1.next = h2
            h2.next = temp1

            h1 = temp1
            h2 = temp2