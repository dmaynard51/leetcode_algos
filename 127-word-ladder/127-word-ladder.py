class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        adj = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + '*' + word[i+1:]
                adj[temp].append(word)
        
        q = deque([beginWord])
        res = 1
        visit = set()
        while q:
            lenQ = len(q)
            
            for i in range(lenQ):
                
                word = q.popleft()
                
                if word == endWord:
                    return res
                visit.add(word)
                for i in range(len(word)):
                    temp = word[:i] + '*' + word[i+1:]
                    
                    for w in adj[temp]:
                        if w in visit:
                            continue
                        q.append(w)
            res += 1
        return 0
                
                    