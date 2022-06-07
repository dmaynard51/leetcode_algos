class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = set()
        
        adj = defaultdict(list)
        
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        def dfs(node):
            if node in visit:
                return False
            if len(adj[node]) == 0:
                return True
            visit.add(node)
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            adj[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True