# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def merge(n1, n2):
            dummy = node = ListNode(-1)
            
            while n1 and n2:
                if n1.val < n2.val:
                    dummy.next = n1
                    n1 = n1.next
                else:
                    dummy.next = n2
                    n2 = n2.next
                dummy = dummy.next
            
            if n1:
                dummy.next = n1
                dummy = dummy.next
            if n2:
                dummy.next = n2
                dummy = dummy.next
            
            return node.next
        
        m = len(lists)//2
        l, r = lists[:m], lists[m:]
        
        left, right = self.mergeKLists(l), self.mergeKLists(r)
        return merge(left, right)
                    