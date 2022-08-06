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
        
        num1 = "".join(getNum(l1))
        num2 = "".join(getNum(l2))
        sm = int(num1) + int(num2)
        sm = str(sm)
        node = dummy = ListNode(0)

        dummy.next = node
        
        for i in range(len(sm)-1, -1, -1):
            n = ListNode(int(sm[i]))
            node.next = n
            node = node.next
        return dummy.next
            
        