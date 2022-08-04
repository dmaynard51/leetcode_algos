# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val]
        
        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            l = max(0, l)
            r = max(0, r)
            res[0] = max(res[0], l + r + node.val)
            return node.val + max(l, r)
        
        dfs(root)
        return res[0]