# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getNum(node):
            res = []
            while node:
                res.append(str(node.val))
                node = node.next
            return res[::-1]
        
        num1 = ''.join(getNum(l1))
        num2 = ''.join(getNum(l2))
        sm = int(num1) + int(num2)
        sm2 = str(sm)
        
        head1 = head2 = ListNode(-1)
        
        for i in range(len(sm2)-1, -1, -1):
            #print sm2[i]
            n = ListNode(int(sm2[i]))
            head2.next = n
            head2 = head2.next
        
        return head1.next
        
        
            