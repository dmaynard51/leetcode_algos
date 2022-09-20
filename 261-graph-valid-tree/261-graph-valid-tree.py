class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        
        visit = set()
        
        adj = defaultdict(list)
        
        for src, nei in edges:
            adj[src].append(nei)
            adj[nei].append(src)
            
        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True
        
        
        
        return dfs(0, -1) and len(visit) == n