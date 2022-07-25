class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        adj = defaultdict(list)
        
        for id, score in items:
            adj[id].append(score)
        
        res = []
        
        for id, score in adj.items():
            score.sort(reverse = True)
            sm = sum(score[:5])//5
            res.append([id,sm])
        #print res
        return res