class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = ['JFK']
        tickets.sort()
        visit = set()
        adj = defaultdict(list)
        
        for src, dst in tickets:
            adj[src].append(dst)
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            temp = list(adj[src])
            for i, nei in enumerate(temp):
                adj[src].pop(i)
                res.append(nei)
                if dfs(nei):
                    return True
                res.pop()
                adj[src].insert(i, nei)
            return False
        dfs('JFK')
        return res