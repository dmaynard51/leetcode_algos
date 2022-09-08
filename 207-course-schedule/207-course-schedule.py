class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        
        for src, nei in prerequisites:
            adj[src].append(nei)
        
        #print adj
        visit = set()
        cycle = set()
        def dfs(node):
            
            if node in cycle:
                return False
            if node in visit:
                return True
                
            cycle.add(node)
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
                
            cycle.remove(node)
            visit.add(node)
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        
        
        
        #1 - > 0 -> F