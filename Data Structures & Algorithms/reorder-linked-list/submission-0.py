# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        # slow is now at the middle
        prev, curr = None, slow.next
        slow.next = None  # break the list into two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # now 'prev' points to the head of the reversed second half

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            # temporarily store next pointers
            tmp1, tmp2 = first.next, second.next
            # link first node to one from second half
            first.next = second
            # link that node to next from first half
            second.next = tmp1
            # move pointers forward
            first, second = tmp1, tmp2

        # No return needed since we modify in-place