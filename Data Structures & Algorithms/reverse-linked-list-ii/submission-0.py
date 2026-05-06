# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #If the list is empty, or reversing a single node range,
        # then no work is needed
        if not head or left == right:
            return head

        # dummy -> 1 -> 2 -> 3 -> 4 -> 5
        # prev stops at node 1
        # curr = 2

        # tempe = 3
        # remove 3 
        # list = 1-> 2-> 4-> 5

        # insert 3 after 1
        # list 1->3->2->4->5

        # temp = 4
        # remove 4 
        # list = 1-> 3-> 2-> 5

        # insert 3 after 1
        # list 1->4->3->2->5

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next 

        curr = prev.next

        for _ in range(right - left):
            temp = curr.next 
            curr.next = temp.next
            temp.next = prev.next 
            prev.next = temp

        return dummy.next