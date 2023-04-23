# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy1 = ListNode(-1)
        dummy1.next = head
        dummy2 = dummy1
        
        count = 0
        
        while head:
            head = head.next
            count += 1
        
        n = count - n
        
        while n != 0:
            dummy1 = dummy1.next
            n -= 1
        
        dummy1.next = dummy1.next.next
        return dummy2.next
        