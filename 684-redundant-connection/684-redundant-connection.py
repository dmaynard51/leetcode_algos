class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        par = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]
        
        def find(node):
            p = par[node]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            
            return p
        
        def union(a, b):
            a1, b1 = find(a), find(b)
            
            if a1 == b1:
                return False
            
            if rank[a1] > rank[b1]:
                par[b1] = a1
                rank[a1] += rank[b1]
            else:
                par[a1] = b1
                rank[b1] += rank[a1]
            return True
        
        for a,b in edges:
            if not union(a, b):
                return [a,b]
                