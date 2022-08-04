# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node, lvl):
            if node:
                if len(res) < lvl + 1:
                    res.append([])
                res[lvl].append(node.val)
                dfs(node.left, lvl + 1)
                dfs(node.right, lvl + 1)
        dfs(root, 0)
        return res