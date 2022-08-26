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
        fst = head
        slow = head
        
        while fst and fst.next:
            fst = fst.next.next
            slow = slow.next
            if fst == slow:
                return True
        return False