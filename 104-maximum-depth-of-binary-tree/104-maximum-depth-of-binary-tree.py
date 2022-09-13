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
        res = [0]
        def dfs(node):
            if node:
                left, right = dfs(node.left), dfs(node.right)
                return 1 + max(left, right)
            else:
                return 0
        return dfs(root)