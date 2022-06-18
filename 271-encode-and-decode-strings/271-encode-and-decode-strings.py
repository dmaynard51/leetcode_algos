class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for w in strs:
            res += (str(len(w)) + '#' + w)
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        
        i = 0
        #print s
        while i < len(s):
            word = ""
            num = ""
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            word = s[j+1:j + 1 +num]
            res.append(word)
            i = j + 1 + num
        return res
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))