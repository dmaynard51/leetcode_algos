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
        
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[-1]
        
        def merge(l, r):
            dummy = ListNode(-1)
            dummy2 = dummy
            
            while l and r:
                if l.val < r.val:
                    dummy.next = l
                    l = l.next
                else:
                    dummy.next = r
                    r = r.next
                dummy = dummy.next
                
            if l:
                dummy.next = l
            
            if r:
                dummy.next = r
                
            
            return dummy2.next
        
        m = len(lists)//2
        left, right = lists[:m], lists[m:]
        
        l, r = self.mergeKLists(left), self.mergeKLists(right)
        return merge(l, r)