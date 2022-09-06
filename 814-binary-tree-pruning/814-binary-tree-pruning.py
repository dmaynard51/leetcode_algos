# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if node:
                node.left, node.right = dfs(node.left), dfs(node.right)
                if node.val == 0 and node.left == None and node.right == None:
                    return None
                return node
        
        return dfs(root)