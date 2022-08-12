# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(p,root, q):
            if root:
                #print p, root.val, q
                if p.val < root.val and root.val < q.val:
                    #print root.val
                    return root
                if root.val < p.val and root.val < q.val:
                    return dfs(p, root.right, q)
                if root.val > p.val and root.val > q.val:
                    return dfs(p, root.left, q)
                return root
        
        return dfs(p,root, q)