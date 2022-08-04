class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = defaultdict(list)
        
        for course, pre in prerequisites:
            adj[course].append(pre)
            
        
        visit = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            #print node, visit
            for pre in adj[node]:
                if not dfs(pre):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        #print visit
        if len(visit) == numCourses:
            return True
        return False
            