# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return [0, True]
            l, r = dfs(root.left), dfs(root.right)
            balanced = l[1] and r[1] and (abs(l[0] - r[0]) <= 1)
            return [1 + max(l[0], r[0]), balanced]
        
        return dfs(root)[1]
            