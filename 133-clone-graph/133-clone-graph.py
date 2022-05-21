"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        dct = defaultdict(list)
        if not node:
            return None
        def dfs(node):
            if node in dct:
                return dct[node]
            temp = Node(node.val)
            dct[node] = temp
            
            for nei in node.neighbors:
                temp.neighbors.append(dfs(nei))
            return dct[node]
        return dfs(node)