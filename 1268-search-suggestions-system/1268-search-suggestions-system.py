class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []
            def add_suggestion(self, product):
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)
        
        products.sort()
        root = TrieNode()
        
        for word in products:
            node = root
            for c in word:
                node = node.children[c]
                node.add_suggestion(word)
        
        res = []
        node = root
        
        for char in searchWord:
            node = node.children[char]
            res.append(node.suggestion)
        return res
            