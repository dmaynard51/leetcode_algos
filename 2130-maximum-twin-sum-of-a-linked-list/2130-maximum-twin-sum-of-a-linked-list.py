# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow, fast = head, head
        res = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        cur = slow
        nxt = slow
        
        while nxt:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        while prev:
            res = max(res, head.val + prev.val)
            prev = prev.next
            head = head.next
        return res