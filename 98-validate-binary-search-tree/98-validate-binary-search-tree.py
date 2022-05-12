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
        
        def dfs(left, node, right):
            if not node:
                return True
            if not (left < node.val and node.val < right):
                return False
            return dfs(left, node.left, node.val) and dfs(node.val, node.right, right)
        
        return dfs(-float('inf'), root, float('inf'))