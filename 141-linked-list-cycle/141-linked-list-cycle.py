# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        cur = head
        fast = head
        if not head:
            return False
        while fast.next and fast.next.next:
            
            fast = fast.next.next
            cur = cur.next
            
            if fast == cur:
                return True
        return False