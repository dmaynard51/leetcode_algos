class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = ['JFK']
        adj = defaultdict(list)
        
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        #print adj
        
        def dfs(node):

            if len(res) == len(tickets)+1:
                return True
            if node not in adj:
                return False            
            
            temp = list(adj[node])
            #print temp
            for i, dst in enumerate(temp):
                adj[node].pop(i)
                res.append(dst)
                if dfs(dst):
                    return True
                adj[node].insert(i, dst)
                res.pop()
            
            
            return False
        dfs('JFK')
        return res