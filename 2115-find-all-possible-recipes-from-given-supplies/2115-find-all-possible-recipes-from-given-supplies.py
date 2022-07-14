class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        ind = {}
        dct = defaultdict(list)
        for r, ing in zip(recipes, ingredients):
            ind[r] = len(ing)
            for i in ing:
                dct[i].append(r)
        
        #print ind, dct
        q = deque(supplies)
        res = []
        
        while q:
            ingredient = q.popleft()
            if ingredient in recipes:
                res.append(ingredient)
            
            for r in dct[ingredient]:
                ind[r] -=1
                
                if ind[r] == 0:
                    q.append(r)
        return res