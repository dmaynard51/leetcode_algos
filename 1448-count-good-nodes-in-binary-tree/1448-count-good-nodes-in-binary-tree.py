# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        
        def dfs(node, mx):
            if node:
                if node.val >= mx:
                    res[0] += 1
                mx = max(mx, node.val)
                dfs(node.left, mx)
                dfs(node.right, mx)
        dfs(root, root.val)
        return res[0]