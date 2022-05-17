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
        def dfs(low, node, high):
            if not node:
                return True
            if not (low < node.val and node.val < high):
                return False
            return dfs(low, node.left, node.val) and dfs(node.val, node.right, high)
        
        return dfs(-float('inf'), root, float('inf'))