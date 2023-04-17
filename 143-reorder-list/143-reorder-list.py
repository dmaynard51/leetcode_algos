# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        
        
        cur = slow
        prev = fast = None
        
        
        while cur:
            fast = cur.next
            cur.next = prev
            prev = cur
            cur = fast

        
        l1 = head
        l2 = prev
        
        while l2.next:
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1,l2.next
            
        
            
            
            
        