class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        
        for src, nei in edges:
            adj[src].append(nei)
            adj[nei].append(src)
        
        
        visit = set()
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