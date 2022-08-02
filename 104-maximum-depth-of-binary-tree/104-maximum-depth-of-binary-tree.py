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
        
        def dfs(r):
            if not r:
                return 0
            if r:
                l, r = dfs(r.left), dfs(r.right)
                
                return 1 + max(l, r)
        
        return dfs(root)