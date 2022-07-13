# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        nxt = head
        cur = head
        prev = None
        
        while nxt:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev