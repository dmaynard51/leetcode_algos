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
            leftMx = dfs(node.left)
            rightMax = dfs(node.right)
            leftMx = max(leftMx, 0)
            rightMax = max(rightMax, 0)
            res[0] = max(res[0], node.val + leftMx + rightMax)
            return node.val + max(leftMx, rightMax)
        dfs(root)
        return res[0]