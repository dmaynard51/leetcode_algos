class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
        adj = defaultdict(list)
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            
            for nei in adj[i]:
                if nei == prev:
                    continue
                elif not dfs(nei, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n