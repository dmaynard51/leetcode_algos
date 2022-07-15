class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """

        users = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):    
            users[user].append(site)     # defaultdicts simplify and optimize code     
        
        patterns = collections.Counter()

        for users, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))
        
        #print patterns
        return max(sorted(patterns), key=patterns.get)
        
