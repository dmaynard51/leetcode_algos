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
        
        def dfs(root):
            if not root:
                return 0
            l = max(dfs(root.left),0)
            r = max(dfs(root.right),0)
            res[0] = max(res[0], l + r + root.val)
            return root.val + max(l, r)
        
        dfs(root)
        return res[0]