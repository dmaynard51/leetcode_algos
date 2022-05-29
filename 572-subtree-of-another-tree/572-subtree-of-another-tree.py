# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        def dfs(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return l.val == r.val and dfs(l.left, r.left) and dfs(l.right, r.right)
        
        self.res = 0
        
        def check(node, sub):
            if node:
                if dfs(node, sub):
                    self.res = True
                check(node.left, sub)
                check(node.right,sub)
            
                
        check(root, subRoot)
        return self.res