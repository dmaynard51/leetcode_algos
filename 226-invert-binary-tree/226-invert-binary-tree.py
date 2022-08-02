# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(r):
            if r:
                r.left, r.right = r.right, r.left
                dfs(r.left)
                dfs(r.right)
            
                return r
        return dfs(root)