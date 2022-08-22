class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visit = set()
        
        adj = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        
        
        def dfs(node):
            if node in visit:
                return 0
            
            visit.add(node)
            
            for nei in adj[node]:
                dfs(nei)
            
            
            return 1
        
        res = 0
        
        for i in range(n):
            res += dfs(i)
        return res
            