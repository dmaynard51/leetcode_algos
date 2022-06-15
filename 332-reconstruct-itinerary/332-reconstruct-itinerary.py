class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = ['JFK']
        adj = defaultdict(list)
        tickets.sort()
        for src, nei in tickets:
            adj[src].append(nei)
        
        
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj:
                return False
            
            temp = list(adj[node])
            
            for i, nei in enumerate(temp):
                res.append(nei)
                adj[node].pop(i)
                if dfs(nei):
                    return True
                res.pop()
                adj[node].insert(i, nei)
            return False
        dfs('JFK')
        return res