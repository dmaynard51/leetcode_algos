class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = {i:[] for i in range(n)}
        
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        
        visit = set()
        
        def dfs(node):
            if node in visit:
                return 0
            
            visit.add(node)
            
            for nei in adj[node]:
                dfs(nei)
            
            return 1
        res = 0
        for i in range((n)):
            if i not in visit:
                res += dfs(i)
        return res