class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        par = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(n):
            res = n
            
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(a, b):
            a1, b1 = find(a), find(b)
            
            if a1 == b1:
                return 0
            
            if rank[b1] > rank[a1]:
                par[a1] = b1
                rank[b1] += rank[a1]
            else:
                par[b1] = a1
                rank[a1] += rank[b1]
            
            return 1
        
        res = n
        
        for a,b in (edges):
            res -= union(a, b)
        return res
            