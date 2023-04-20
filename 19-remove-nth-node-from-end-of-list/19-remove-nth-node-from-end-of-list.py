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
            count+=1 
            head = head.next
        
        count = count - n
        # dummy1 = dummy1.next
        while count != 0:
            dummy1 = dummy1.next
            count -= 1
            
        
        dummy1.next = dummy1.next.next
        
        return dummy2.next