# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        def dfs(node):
            if node:
                self.res.append(str(node.val))
                
                if not node.left and not node.right:
                    return
                self.res.append('(')
                dfs(node.left)
                self.res.append(')')
                
                if node.right:
                    self.res.append('(')
                    dfs(node.right)
                    self.res.append(')')
                    
                    
                
                
        
        dfs(root)
        return ''.join(self.res)
        