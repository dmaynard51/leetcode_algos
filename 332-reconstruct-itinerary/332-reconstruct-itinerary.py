class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj = {src:[] for src,dst in tickets}
        
        tickets.sort()
        
        for src, dst in tickets:
            adj[src].append(dst)
        res = ['JFK']
        
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, dst in enumerate(temp):
                adj[src].pop(i)
                res.append(dst)
                if dfs(dst):
                    return True
                adj[src].insert(i, dst)
                res.pop()
            return False
        
        dfs('JFK')
        return res
        