class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        users = defaultdict(list)
        
        for user, time, web in sorted(zip(username, timestamp, website)):
            users[user].append(web)
            
        counter = collections.Counter()
        
        for user, website in users.items():
            counter.update(Counter(set(combinations(website, 3))))
        
        return max(sorted(counter), key = counter.get)