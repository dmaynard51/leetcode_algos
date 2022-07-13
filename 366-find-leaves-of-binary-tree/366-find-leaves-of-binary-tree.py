# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node):
            if not node:
                return -1
            height = max(dfs(node.left), dfs(node.right)) + 1
            if height >= len(res):
                res.append([])
            res[height].append(node.val)
            return height
        dfs(root)
        return res