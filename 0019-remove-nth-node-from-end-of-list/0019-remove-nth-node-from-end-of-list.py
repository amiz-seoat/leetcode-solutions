# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to handle edge cases (like removing head)
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast pointer n+1 steps ahead to create gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Now slow is just before the node to delete
        slow.next = slow.next.next

        return dummy.next
