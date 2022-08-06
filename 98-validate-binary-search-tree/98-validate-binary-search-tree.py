# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check(l, node, r):
            if not node:
                return True
            if not (l < node.val and node.val < r):
                return False
            return check(l, node.left, node.val) and check(node.val, node.right, r)
        
        return check(-float('inf'), root, float('inf'))