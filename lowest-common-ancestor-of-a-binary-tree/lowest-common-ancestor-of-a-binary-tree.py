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
        adj = {root:None}
        visit = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                adj[node.left] = node
                stack.append(node.left)
            if node.right:
                adj[node.right] = node
                stack.append(node.right)
        
        #print adj
        while p:
            visit.add(p)            
            p = adj[p]

            
        while q not in visit:
            visit.add(q)  
            q = adj[q]
        
        return q
        