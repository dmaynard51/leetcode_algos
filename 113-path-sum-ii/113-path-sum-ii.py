# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(node, target, path):
            if node:
                path.append(node.val)
                if node.val == target and not node.left and not node.right:
                    res.append(path[:])
                dfs(node.left, target- node.val, path)
                dfs(node.right, target- node.val, path)
                if path:
                    path.pop()
        
        dfs(root, targetSum, [])
        return res
                