# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = 0
        
        q = []
        
        cur = root
        
        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            res += 1
            
            if res == k:
                return cur.val
            cur = cur.right