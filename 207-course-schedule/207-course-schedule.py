class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preReq = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preReq[crs].append(pre)
        
        visit = set()
        
        def dfs(node):
            if node in visit:
                return False
            if len(preReq[node]) == 0:
                return True
            visit.add(node)
            
            for pre in preReq[node]:
                if not dfs(pre):
                    return False
            visit.remove(node)
            preReq[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True