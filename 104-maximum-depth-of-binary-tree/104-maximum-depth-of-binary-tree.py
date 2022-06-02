# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            return 1 + max(left, right)
        
        return dfs(root)