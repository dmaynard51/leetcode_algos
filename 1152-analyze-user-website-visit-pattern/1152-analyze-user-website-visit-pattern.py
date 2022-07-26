class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        adj = defaultdict(list)
        
        for user, time, site in sorted(zip(username, timestamp, website)):
            adj[user].append(site)
        
        counter = collections.Counter()
        for user, website in adj.items():
            counter.update(Counter(set(combinations(website,3))))
        mx = 0
        user = ()
        #print counter
        for u, val in sorted(counter.items()):
            if val > mx:
                mx = val
                user = u
        
        return (user)