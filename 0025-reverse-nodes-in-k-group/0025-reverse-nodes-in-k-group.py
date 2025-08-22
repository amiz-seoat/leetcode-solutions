# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper: reverse linked list from start to end
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # new head of reversed group

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:  # not enough nodes
                    return dummy.next

            group_next = kth.next
            # Reverse the group
            start = group_prev.next
            kth.next = None
            new_head = reverse(start, None)
            
            # Connect reversed group back
            group_prev.next = new_head
            start.next = group_next

            # Move to next group
            group_prev = start
