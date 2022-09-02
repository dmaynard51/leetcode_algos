# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.res = []
        
        def dfs(node, lvl):
            if node:
                if len(self.res) < lvl + 1:
                    self.res.append([])
                self.res[lvl].append(node.val)
                dfs(node.left, lvl+1)
                dfs(node.right, lvl + 1)
        
        dfs(root, 0)
        res2 = []
        for lvl in self.res:
            res2.append(sum(lvl)/float(len(lvl)))
        
        return res2