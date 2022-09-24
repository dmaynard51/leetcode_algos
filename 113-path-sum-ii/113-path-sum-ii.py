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
        def dfs(node, path, sm):
            if node:
                path.append(node.val)
                if node.val == sm and not node.left and not node.right:
                    res.append(path[:])
                dfs(node.left, path, sm - node.val)
                dfs(node.right, path, sm - node.val)
                if path:
                    path.pop()
        
        dfs(root, [], targetSum)

        return res