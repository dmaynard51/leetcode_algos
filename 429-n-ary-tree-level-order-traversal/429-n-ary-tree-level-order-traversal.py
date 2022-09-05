"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(node, lvl):
            if node:
                if len(self.res) < lvl + 1:
                    self.res.append([])
                self.res[lvl].append(node.val)
                for i in (node.children):
                    dfs(i, lvl +1)
        
        dfs(root, 0)
        return self.res
        