class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        class TrieNode():
            def __init__(self):
                self.neighbors = defaultdict(TrieNode)
                self.suggestions = []

            def addSuggestion(self,suggestion):
                if len(self.suggestions) < 3:
                    self.suggestions.append(suggestion)
        
        root = TrieNode()
        
        products.sort()
        curr = root
        for word in products:
            curr = root
            for c in word:
                curr = curr.neighbors[c]
                curr.addSuggestion(word)
        
        res = []
        curr = root
        for c in searchWord:
            curr = curr.neighbors[c]
            res.append(curr.suggestions)
        
        return res
                