class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in string.lowercase}
        #print uf
        for a, e, _, b in equations:
            if e == "=":

                uf[find(a)] = find(b)
                #print uf                
        
        
        for a, e, _, b in equations:
            if e == '!':
                if find(a) == find(b):
                    return False
        return True