class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        adj = defaultdict(list)
        #log
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj[pattern].append(word)
        
        visit = set()
        res = 1
        q = deque([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for w in adj[pattern]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)

                
            
            res +=1
        return 0
                
            
            
            
            