class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        u = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website)):
            u[user].append(web)
            
        counter = collections.Counter()
        
        mx = ""
        for user, website in u.items():
            counter.update(Counter(set(combinations(website, 3))))
        #print counter
        
        
        
        return max(sorted(counter), key = counter.get)                   
                           