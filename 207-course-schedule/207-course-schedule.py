class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = set()
        cycle = set()
        
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visit.add(node)
            cycle.remove(node)
            return True
        
        for i in range((numCourses)):
            if not dfs(i):
                return False
        #print len(visit)
        if len(visit) == (numCourses):
            return True